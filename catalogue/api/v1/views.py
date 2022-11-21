# python imports

# django imports
from django.db.models import Q
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
import pdb
# third party imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import (
    status,
    viewsets,
    mixins,
    permissions,
    response,
)
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)

# inner app imports
from catalogue.models import (
    DietitionsAndNutritionists,
    Product,
    Category,
    BannerImages,
)
from canleath.utils import parse_basket_from_hyperlink
from checkout.models import UserTransaction
from shipping.repository import Repository

# local imports
from .serializers import (
    DietitionsAndNutritionistSerializer,
    ProductListSerializer,
    CategorySerializer,
    BannerImagesSerializer,
    BasketSerializer,
    BasketLineSerializer,
    CustomAddProductSerializer,
    OrderSerializer,
    CheckoutSerializer,
    OrderLineSerializer,
    OrderUpdateSerializer,
    QuestionaireSerializer,
    VoucherRemoveSerializer,
)
from .pagination import ObjectPagination2x

# oscar imports
from oscar.core.loading import get_class, get_model
from oscar.apps.payment.exceptions import PaymentError
from oscar.apps.basket import signals

# oscar api imports
from oscarapi.views import (
    basket,
    basic,
)
from oscarapi.basket import operations

from oscarapi.views import checkout as corecheckout
from oscarapi.basket.operations import request_allows_access_to_basket
from oscarapi.signals import oscarapi_post_checkout
from oscarapi.permissions import IsOwner

Order = get_model("order", "Order")
OrderLine = get_model("order", "Line")
OrderNote = get_model('order', 'OrderNote')
EventHandler = get_class('order.processing', 'EventHandler')


class CategoryApiViewSet(viewsets.GenericViewSet,
                         mixins.RetrieveModelMixin,
                         mixins.ListModelMixin,
                         ):
    """
    Viewset for category list
    """

    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(is_active=True)


class ProductApiViewSet(viewsets.GenericViewSet,
                         mixins.RetrieveModelMixin,
                         mixins.ListModelMixin,
                         ):
    """
    List View for blog search
    """

    serializer_class = ProductListSerializer
    pagination_class = ObjectPagination2x

    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True).exclude(structure='child')

        if self.request.GET.getlist('category'):
            get_category_list = self.request.GET.getlist('category')
            queryset = queryset.filter(categories__in=get_category_list)

        if self.request.GET.get('is_latest_product', None) == '1':
            queryset = queryset.filter(is_latest_product=True)

        if self.request.GET.get('min_price') and self.request.GET.get('max_price'):
            min_price = int(self.request.GET.get('min_price'))
            max_price = int(self.request.GET.get('max_price'))
            queryset = queryset.filter(stockrecords__price_excl_tax__range=[min_price,max_price])

        if self.request.GET.get('query'):
            get_query = self.request.GET.get('query')
            queryset = queryset.filter(
                Q(title__icontains=get_query)
            )

        return queryset


class BannerImageApiViewSet(viewsets.GenericViewSet,
                            mixins.RetrieveModelMixin,
                            mixins.ListModelMixin):
    """
    List View for Banner Image
    """

    serializer_class = BannerImagesSerializer
    pagination_class = ObjectPagination2x

    def get_queryset(self):
        queryset = BannerImages.objects.all()

        if self.request.GET.get('is_active', None):
            queryset = queryset.filter(is_active=True)

        return queryset


class BasketView(basket.BasketView):
    """
    Customised Basket View

    Api for retrieving a user's basket.

    GET:
    Retrieve your basket
    """
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = BasketSerializer


class BasketList(basic.BasketList):
    """
    Custom Basket List View
    Retrieve all baskets that belong to the current (authenticated) user.
    """
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = BasketSerializer

class BasketDetail(basic.BasketDetail):
    """
    Custom Basket Detail View
    """
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = BasketSerializer


class LineList(basket.LineList):
    """
    Api for adding lines to a basket.

    Permission will be checked,
    Regular users may only access their own basket,
    staff users may access any basket.

    GET:
    A list of basket lines.

    POST(basket, line_reference, product, stockrecord,
         quantity, price_currency, price_excl_tax, price_incl_tax):
    Add a line to the basket, example::

        {
            "basket": "http://127.0.0.1:8000/oscarapi/baskets/100/",
            "line_reference": "234_345",
            "product": "http://127.0.0.1:8000/oscarapi/products/209/",
            "quantity": 3,
            "price_currency": "EUR",
            "price_excl_tax": "100.0",
            "price_incl_tax": "121.0"
        }
    """

    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = BasketLineSerializer


class BasketLineDetail(basket.BasketLineDetail):
    """
    Only the field `quantity` can be changed in this view.
    All other fields are readonly.
    """

    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = BasketLineSerializer


class AddProductView(basket.AddProductView):
    """
    Add a certain quantity of a product to the basket.

    POST(url, quantity)
    {
        "url": "http://testserver.org/oscarapi/products/209/",
        "quantity": 6
    }

    If you've got some options to configure for the product to add to the
    basket, you should pass the optional ``options`` property:
    {
        "url": "http://testserver.org/oscarapi/products/209/",
        "quantity": 6,
        "options": [{
            "option": "http://testserver.org/oscarapi/options/1/",
            "value": "some value"
        }]
    }
    """
    # permission_classes = (permissions.IsAuthenticated,)
    add_product_serializer_class = CustomAddProductSerializer
    serializer_class = BasketSerializer

    def post(self, request, *args, **kwargs):  # pylint: disable=redefined-builtin
        # pdb.set_trace()
        p_ser = self.add_product_serializer_class(
            data=request.data, context={"request": request}
        )
        if p_ser.is_valid():
            basket = operations.get_basket(request)
            product = p_ser.validated_data["url"]
            quantity = p_ser.validated_data["quantity"]
            options = p_ser.validated_data.get("options", [])

            basket_valid, message = self.validate(basket, product, quantity, options)
            if not basket_valid:
                return Response(
                    {"reason": message}, status=status.HTTP_406_NOT_ACCEPTABLE
                )

            basket.add_product(product, quantity=quantity, options=options)

            signals.basket_addition.send(
                sender=self, product=product, user=request.user, request=request
            )

            operations.apply_offers(request, basket)
            ser = self.serializer_class(basket, context={"request": request})
            response_data = ser.data
            if basket.lines.filter(product=product).exists():
                response_data['current_line_id'] = basket.lines.filter(product=product).first().id
            return Response(response_data)

        return Response({"reason": p_ser.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)





class ValidateCheckoutView(corecheckout.CheckoutView):
   
    permission_classes = (permissions.IsAuthenticated,)
    order_serializer_class = OrderSerializer
    serializer_class = CheckoutSerializer

    def post(self, request, format=None, *args, **kwargs):
        # TODO: Make it possible to create orders with options.
        # at the moment, no options are passed to this method, which means they
        # are also not created.
        
        basket = parse_basket_from_hyperlink(request.data, format)

        if not request_allows_access_to_basket(request, basket):
            return response.Response(
                "Unauthorized", status=status.HTTP_401_UNAUTHORIZED
            )

        c_ser = self.serializer_class(data=request.data, context={"request": request})

        if c_ser.is_valid():
            return response.Response({"status":"checkout data validated"}, status.HTTP_200_OK)
            
        return response.Response(c_ser.errors, status.HTTP_406_NOT_ACCEPTABLE)




class CheckoutView(corecheckout.CheckoutView):
    """
    Prepare an order for checkout.

    POST(basket, shipping_address,
         [total, shipping_method_code, shipping_charge, billing_address]):
    {
        "basket": "http://testserver/oscarapi/baskets/1/",
        "guest_email": "foo@example.com"(optional),
        "total": "100.0",
        "shipping_charge": {
            "currency": "EUR",
            "excl_tax": "10.0",
            "tax": "0.6"
        },
        "shipping_method_code": "no-shipping-required",
        "shipping_address": {
            "country": "http://127.0.0.1:8000/oscarapi/countries/IN/",
            "first_name": "Henk",
            "last_name": "Van den Heuvel",
            "line1": "Roemerlaan 44",
            "line2": "",
            "line3": "",
            "line4": "Kroekingen",
            "notes": "Niet STUK MAKEN OK!!!!",
            "phone_number": "+31 26 370 4887",
            "postcode": "7777KK",
            "state": "Gerendrecht",
            "title": "Mr"
        }
        "billing_address": {
            "country": country_url,
            "first_name": "Jos",
            "last_name": "Henken",
            "line1": "Boerderijstraat 19",
            "line2": "",
            "line3": "",
            "line4": "Zwammerdam",
            "notes": "",
            "phone_number": "+31 27 112 9800",
            "postcode": "6666LL",
            "state": "Gerendrecht",
            "title": "Mr"
         }
    }
    returns the order object.
    """
    permission_classes = (permissions.IsAuthenticated,)
    order_serializer_class = OrderSerializer
    serializer_class = CheckoutSerializer

    def post(self, request, format=None, *args, **kwargs):
        # TODO: Make it possible to create orders with options.
        # at the moment, no options are passed to this method, which means they
        # are also not created.
        

        user_transaction_id = request.data.get('user_transaction_id', None)
        
        # import ipdb;ipdb.set_trace()
        basket = parse_basket_from_hyperlink(request.data, format)

        if not request_allows_access_to_basket(request, basket):
            return response.Response(
                "Unauthorized", status=status.HTTP_401_UNAUTHORIZED
            )

        c_ser = self.serializer_class(data=request.data, context={"request": request})

        if c_ser.is_valid():
            order = c_ser.save()
            if user_transaction_id:
                transaction_obj = get_object_or_404(UserTransaction, id=user_transaction_id)
                transaction_obj.order = order
                transaction_obj.order_number = order.id
                transaction_obj.save()

            if hasattr(settings, 'OSCAR_INITIAL_ORDER_STATUS'):
                order_status = getattr(settings, 'OSCAR_INITIAL_ORDER_STATUS')
                order.status = order_status
                order.payment_done = True
                order.save()
            basket.freeze()

            o_ser = self.order_serializer_class(order, context={"request": request})

            resp = response.Response(o_ser.data, status=status.HTTP_200_OK)

            oscarapi_post_checkout.send(
                sender=self,
                order=order,
                user=request.user,
                request=request,
                response=resp,
            )
            data={
                'order_number': order.number,
                'checkout_order_id':order.id,
            }
            request.session['checkout_order_id'] = order.id
            request.session['order_data'] = data
            return resp


        return response.Response(c_ser.errors, status.HTTP_406_NOT_ACCEPTABLE)


class OrderList(ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = (IsOwner,)

    def get_queryset(self):
        qs = Order.objects.all()
        return qs.filter(user=self.request.user)


class OrderDetail(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsOwner,)


class OrderLineList(ListAPIView):
    queryset = OrderLine.objects.all()
    serializer_class = OrderLineSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        user = self.request.user
        return super().get_queryset().filter(order_id=pk, order__user=user)


class OrderLineDetail(RetrieveAPIView):
    queryset = OrderLine.objects.all()
    serializer_class = OrderLineSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return super().get_queryset().filter(order__user=self.request.user)


class OrderUpdateApiView(UpdateAPIView):
    """
    Update View for Order Detail
    """
    permission_classes = (IsOwner,)
    serializer_class = OrderUpdateSerializer
    queryset = Order.objects.all()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        
        if 'status' in serializer.validated_data:
            new_status = serializer.validated_data.get('status')
            order = instance
            old_status = instance.status
            handler = EventHandler(request.user)
            try:
                handler.handle_order_status_change(order, new_status)
            except PaymentError as e:
                message = "Unable to change order status due to payment error {}".format(e)
                Response({'message': message}, status=status.HTTP_400_BAD_REQUEST)
            else:
                message = "Order status changed from {}s to {}".format(old_status, new_status)
                order.notes.create(
                    user=request.user, message=message, note_type=OrderNote.SYSTEM)
        serializer.save()
        return Response(serializer.data)


class AddVoucherView(basket.AddVoucherView):
    """
    Add a voucher to the basket.

    POST(vouchercode)
    {
        "vouchercode": "kjadjhgadjgh7667"
    }

    Will return 200 and the voucher as json if succesful.
    If unsuccessful, will return 406 with the error.
    """

    # permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):  # pylint: disable=redefined-builtin
        v_ser = self.add_voucher_serializer_class(
            data=request.data, context={"request": request}
        )
        if v_ser.is_valid():
            basket = operations.get_basket(request)

            voucher = v_ser.instance
            basket.vouchers.add(voucher)

            signals.voucher_addition.send(sender=None, basket=basket, voucher=voucher)

            # Recalculate discounts to see if the voucher gives any
            operations.apply_offers(request, basket)
            discounts_after = basket.offer_applications

            # Look for discounts from this new voucher
            for discount in discounts_after:
                if discount["voucher"] and discount["voucher"] == voucher:
                    break
            else:
                basket.vouchers.remove(voucher)
                return Response(
                    {
                        "reason": _(
                            "Your basket does not qualify for a voucher discount"
                        )
                    },  # noqa
                    status=status.HTTP_406_NOT_ACCEPTABLE,
                )

            ser = self.serializer_class(voucher, context={"request": request})
            return Response(ser.data)

        return Response(v_ser.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class VoucherRemoveApiView(APIView):
    """
    Api view for remove voucher
    """

    permission_classes = (permissions.IsAuthenticated,)
    remove_voucher_serializer = VoucherRemoveSerializer
    remove_signal = signals.voucher_removal

    def post(self, request, *args, **kwargs):
        v_ser = self.remove_voucher_serializer(
            data=request.data, context={'request': request,}
        )
        if v_ser.is_valid():
            basket = operations.get_basket(request)
            voucher = v_ser.instance
            request.basket.vouchers.remove(voucher)
            self.remove_signal.send(
                sender=self, basket=request.basket, voucher=voucher)
            return Response(data={'message': 'Voucher Removed from Cart'}, status=status.HTTP_200_OK)
            # return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(v_ser.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class ShippingMethodView(basket.ShippingMethodView):
    """
    Custom Shipping Method View
    """

    def _get(self, request, shipping_address=None):  # pylint: disable=redefined-builtin
        basket = operations.get_basket(request)
        shiping_methods = Repository().get_shipping_methods(
            basket=basket,
            user=request.user,
            shipping_addr=shipping_address,
            request=request,
        )
        ser = self.shipping_method_serializer_class(
            shiping_methods, many=True, context={"basket": basket}
        )
        return Response(ser.data)        



class DietitionsAndNutritionistsApiViewSet(viewsets.GenericViewSet,
                            mixins.RetrieveModelMixin,
                            mixins.ListModelMixin):
    """
    List View for DietitionsAndNutritionists
    """

    serializer_class = DietitionsAndNutritionistSerializer
    pagination_class = ObjectPagination2x

    def get_queryset(self):
        queryset = DietitionsAndNutritionists.objects.all()

        return queryset



class QuestionaireCreateApiView(APIView):
    """
    Api view for questionaire create
    """
    
    def post(self, request, *args, **kwargs):
        serializer = QuestionaireSerializer(data=request.data)
        if serializer.is_valid():
            questionaire = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
