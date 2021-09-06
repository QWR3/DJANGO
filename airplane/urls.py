from django.urls import path

from .views import Airplane_list_get_create, Airplane_read_update_delete

urlpatterns = [
    path('', Airplane_list_get_create.as_view(), name='airplane_list_create'),
    path('<int:pk>/', Airplane_read_update_delete.as_view(), name='airplane_read_update_delete'),
]
