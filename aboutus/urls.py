from django.urls import path
from . import views


urlpatterns = [
    path('', views.aboutus_list, name='aboutus'),
]