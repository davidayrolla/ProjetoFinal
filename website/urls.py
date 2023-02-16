from django.urls import path, re_path, include
from .views import home

urlpatterns = [
    re_path(r'^$', home, name='website_home'),
]