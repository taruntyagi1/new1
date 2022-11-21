# oscar imports
from oscar.apps.dashboard.tables import DashboardTable
from catalogue.models import Category, Product

# django imports
from django_tables2 import A, Column, LinkColumn, TemplateColumn
from django.utils.safestring import mark_safe
from django.utils.translation import ungettext_lazy
from django.utils.translation import gettext_lazy as _

class CategoryTable(DashboardTable):
    name = LinkColumn('dashboard:catalogue-category-update', args=[A('pk')])
    description = TemplateColumn(
        template_code='{{ record.description|default:""|striptags'
                      '|cut:"&nbsp;"|truncatewords:6 }}')
    # mark_safe is needed because of
    # https://github.com/bradleyayers/django-tables2/issues/187

    actions = TemplateColumn(
        template_name='catalogue/category_row_actions.html',
        orderable=False)

    icon = "sitemap"
    caption = ungettext_lazy("%s Category", "%s Categories")

    class Meta(DashboardTable.Meta):
        model = Category
        fields = ('name', 'description')


class ProductTable(DashboardTable):
    title = TemplateColumn(
        verbose_name=_('Title'),
        template_name='oscar/dashboard/catalogue/product_row_title.html',
        order_by='title', accessor=A('title'))
    image = TemplateColumn(
        verbose_name=_('Image'),
        template_name='oscar/dashboard/catalogue/product_row_image.html',
        orderable=False)
    product_class = Column(
        verbose_name=_('Product type'),
        accessor=A('product_class'),
        order_by='product_class__name')
    stock_records = TemplateColumn(
        verbose_name=_('Stock records'),
        template_name='oscar/dashboard/catalogue/product_row_stockrecords.html',
        orderable=False)
    is_latest_product = Column(
        verbose_name=_('Is Latest'),
        accessor=A('is_latest_product'),
        order_by='is_latest_product'
    )
    actions = TemplateColumn(
        verbose_name=_('Actions'),
        template_name='oscar/dashboard/catalogue/product_row_actions.html',
        orderable=False)

    icon = "sitemap"

    class Meta(DashboardTable.Meta):
        model = Product
        fields = ('upc', 'date_updated')
        sequence = ('title', 'upc', 'image', 'product_class',
                    'stock_records', '...', 'date_updated', 'is_latest_product', 'actions')
        order_by = '-date_updated'