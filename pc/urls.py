from django.urls import path

from .views import PC_list_get_create, PC_read_update_delete

urlpatterns = [
    path('', PC_list_get_create.as_view()),
    path('<int:pk>/', PC_read_update_delete.as_view()),
]