from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    # path('', views.post_details, name='post_details'),
    path('<int:id>', views.post_details, name='post_details'),
]
