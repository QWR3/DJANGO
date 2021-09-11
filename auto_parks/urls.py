from django.urls import path

from .views import AutoParkListCreateView, AutoParkRetrieveUpdateDestroyView, AutoParkCrateCar

urlpatterns = [
    path('', AutoParkListCreateView.as_view(), name='auto_park_list_create'),
    path('<int:pk>', AutoParkRetrieveUpdateDestroyView.as_view(), name='auto_park_retrieve_update_destroy_create'),
    path('<int:pk>/cars', AutoParkCrateCar.as_view(), name='create_car_from_auto_park'),
]
