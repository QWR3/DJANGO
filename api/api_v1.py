from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('apps.auth_.urls')),
    path('users/', include('apps.user.urls'))
]
