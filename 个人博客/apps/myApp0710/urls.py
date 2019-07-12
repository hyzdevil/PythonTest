from django.urls import path, re_path
from apps.myApp0710 import views

app_name = 'myApp0710'

urlpatterns = [
    re_path(r'^$', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('listpic/', views.listpic, name="listpic"),
    path('newslistpic/', views.newslistpic, name="newslistpic"),
]