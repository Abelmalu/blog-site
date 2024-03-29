from django.urls import path
from django.urls import re_path
from . import views 

urlpatterns=[
    path('',views.article_list, name='home'),
    path('about/',views.about, name='about'),
    path('articles/', views.article_list, name='list'),
    path('articles/create',views.article_create, name='create'),
    path('articles/profile/', views.profile, name='profile'),
    path('articles/update<str:pk>',views.update_article, name='update'),
    path('articles/delete<str:pk>',views.delete_article, name='delete'),
    path('articles/<slug:slug>/',views.article_detail, name='detail'),
    path('articles/category/<str:pk>',views.categories, name='category'),
    
    
]