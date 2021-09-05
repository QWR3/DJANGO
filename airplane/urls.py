from django.urls import path

from .views import Airplane_list_get_create

urlpatterns = [
    path('', Airplane_list_get_create.as_view(), name='airplane_list_create')
]
