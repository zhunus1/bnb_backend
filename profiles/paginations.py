from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'page_size'  # Define the query parameter for page size

    def get_page_size(self, request):
        # Override get_page_size to allow clients to specify the page size
        page_size = request.query_params.get(self.page_size_query_param)
        if page_size:
            return int(page_size)
        return super().get_page_size(request)