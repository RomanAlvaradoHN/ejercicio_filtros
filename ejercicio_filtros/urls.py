from django.urls import path
from . import views

urlpatterns = [
    path('', views.ver_index, name='url_ver_index'),
]