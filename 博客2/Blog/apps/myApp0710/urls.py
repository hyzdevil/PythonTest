from django.urls import path, re_path
from apps.myApp0710 import views

app_name = 'myApp0710'

urlpatterns = [
    re_path(r'^$', views.index, name="index"),
    path('resume/', views.resume, name="resume"),
    path('listpic/', views.listpic, name="listpic"),
    re_path(r'newslistpic/(?P<pid>\d+)/', views.newslistpic, name="newslistpic"),
    re_path(r'note/(?P<nid>\d+)/', views.note, name="note"),
    path('leavemessage/', views.leave_message, name="leave_message"),
    re_path(r'messageboard/(?P<mid>\d+)/', views.message_board, name="message_board"),
]