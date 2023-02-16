from django.urls import path, re_path, include
from .views import home, contato

urlpatterns = [
    re_path(r'^$', home, name='website_home'),
    re_path(r'home', home, name='website_home'),
    re_path(r'contato', contato, name='website_contato'),
]