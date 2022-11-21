from order.models import Order
from oscar.apps.dashboard.orders.views import OrderDetailView

class CustomizedOrderDetailView(OrderDetailView):
    """
    Dashboard view to display a single order.

    Supports the permission-based dashboard.
    """
    model = Order
    context_object_name = 'order'
    template_name = 'orders/order_detail.html'

    