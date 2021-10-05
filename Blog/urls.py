from django.urls import path
from . import views

app_name="Blog"

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('details/<pk>', views.blog_details, name='blog_details'),
    path('liked/<pk>', views.liked, name='liked_post'),
    path('unliked/<pk>', views.unliked, name='unliked_post'),
]
