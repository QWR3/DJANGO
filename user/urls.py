from django.urls import path

from user.views import (
    UserActivateView,
    UserDeactivateView,
    UserDoSuperuserView,
    UserDoUserView,
    UserListCreateView,
    UserRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_list_create_view'),
    path('<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user_retrieve_update_destroy_view'),
    path('<int:pk>/activate/', UserActivateView.as_view(), name='user_activate_view'),
    path('<int:pk>/deactivate/', UserDeactivateView.as_view(), name='user_deactivate_view'),
    path('<int:pk>/doUser/', UserDoUserView.as_view(), name='user_do_user_view'),
    path('<int:pk>/doSuperuser/', UserDoSuperuserView.as_view(), name='user_do_superuser_view'),
]
