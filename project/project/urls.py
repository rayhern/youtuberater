
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token
from .views import index, favicon

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('auth/', obtain_auth_token),
    path("", index, name='index'),
    path('favicon.ico', favicon, name='favicon')
]
