from rest_framework.pagination import PageNumberPagination


class MyPagination(PageNumberPagination):
    page_size = 3
    max_page_size = 10
    page_size_query_description = 'size'
    page_query_param = 'page'
