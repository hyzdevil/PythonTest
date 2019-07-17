from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse
from myApp0710.models import *

# Create your views here.
# 首页
def index(request):
    return render(request, 'myApp0710/index.html')
# 个人简介
def resume(request):
    return render(request, 'myApp0710/resume.html')
# 个人相册
def listpic(request):
    return render(request, 'myApp0710/listpic.html')
# 笔记列表页
def newslistpic(request, pid=1):
    p = int(pid)
    artical = Artical.objects.order_by("id")
    page = Paginator(artical, 6)
    artical_page = page.page(p)
    return render(request, 'myApp0710/newslistpic.html', locals())
# 笔记详情页
def note(request, nid):
    artical = Artical.objects.get(id=nid)
    content = artical.content.split("\r\n")
    return render(request, 'myApp0710/notes.html', locals())
# 留言功能
def leave_message(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        LeaveMessage.objects.create(name=name, message=message, phone=phone, email=email)
        return HttpResponse("保存留言成功")
    return render(request, 'myApp0710/leave_message.html', locals())
# 留言板
def message_board(request, mid=1):
    mid = int(mid)
    messageBoard = LeaveMessage.objects.order_by("-date")
    paginator = Paginator(messageBoard, 6)
    page = paginator.page(mid)
    return render(request, 'myApp0710/mrssage_board.html', locals())