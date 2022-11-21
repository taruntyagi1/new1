from rest_framework.pagination import PageNumberPagination

class ObjectPagination2x(PageNumberPagination):
    """
    Object Pagination For Diet History
    """
    page_size = 20