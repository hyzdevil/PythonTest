import time
import random
from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello world!")

# def index_1(request, name):
#     return HttpResponse("Hello world! {}".format(name))

def index_1(request, name):
    return HttpResponse("Hello {}, 现在是北京时间 {}".format(name, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

def get_time(request,m,d):
    m,d = int(m), int(d)
    action = time.struct_time((2019,m,d,0,0,0,0,0,0))
    action = time.mktime(action)
    now = time.localtime(action).tm_yday
    str_time = "%s-%s 是今年的第 %s 天"%(m,d,now)
    return HttpResponse(str_time)

def people_hobby(request):
    dists = {
        "student":[
            {
                "name":"张三",
                "age":18,
                "hobby":["吃饭", "睡觉", "玩游戏", "唱K", "LOL"],
                "picture":"http://n.sinaimg.cn/sinacn21/600/w1920h1080/20180716/664f-hfkffak8292148.jpg"
            },
            {
                "name": "李四",
                "age": 24,
                "hobby": ["吃饭", "睡觉", "打豆豆", "抽烟", "喝酒", "烫头"],
                "picture": "http://img.hookbase.com/img2017/5/5/2017050588356372.jpg"
            },
            {
                "name": "王五",
                "age": 20,
                "hobby": ["吃饭", "睡觉", "打豆豆", "抽烟", "喝酒", "烫头"],
                "picture": "http://img.game333.net/uploads/shouyou/2016/03/14/2016031411523053.jpg"
            },
            {
                "name": "赵六",
                "age": 30,
                "hobby": ["吃饭", "睡觉", "打豆豆", "抽烟", "喝酒", "烫头"],
                "picture": "http://img3.sc115.com/hb/yl2/11/881803014316080.jpg"
            },
            {
                "name": "马七",
                "age": 35,
                "hobby": ["吃饭", "睡觉", "打豆豆", "抽烟", "喝酒", "烫头"],
                "picture": "http://img.mp.itc.cn/upload/20161017/a91bfd46c14a441a985fb92526b8608c_th.jpg"
            },
            {
                "name": "刘八",
                "age": 33,
                "hobby": ["吃饭", "睡觉", "打豆豆", "抽烟", "喝酒", "烫头"],
                "picture": "http://5b0988e595225.cdn.sohucs.com/q_70,c_zoom,w_640/images/20190218/cab276b582c84476bfc590e427fb34c2.jpeg"
            }
        ]
    }
    return render(request, "myApp/index.html", dists)

def work(request):
    dist = {
        "image":[
            {"pict": [{"img": "images/timg0.jpg", "name": "百里守约", "username":"国服骚猪"}]},
            {"pict": [{"img": "images/timg1.jpg", "name": "白色死神 白起", "username":"123木头人"}]},
            {"pict": [{"img": "images/timg2.jpg", "name": "赵云", "username":"斜45度亲你"},{"img": "images/timg9.jpg", "name": "忍·炎影 赵云", "username":"斜45度亲你"}]},
            {"pict": [{"img": "images/timg3.jpg", "name": "荒野大镖客 牛魔", "username":"淡粉色"}]},
            {"pict": [{"img": "images/timg4.jpg", "name": "不知火舞", "username":"呆妹狂魔"}]},
            {"pict": [{"img": "images/timg5.jpg", "name": "高渐离", "username":"你好骚啊"}]},
            {"pict": [{"img": "images/timg6.jpg", "name": "武则天", "username":"agfdsg"}]},
            {"pict": [{"img": "images/timg7.jpg", "name": "爱与和平 程咬金", "username":"别抢猪啊"},{"img": "images/timg11.jpg", "name": "星际陆战队 程咬金", "username":"别抢猪啊"}]},
            {"pict": [{"img": "images/timg8.jpg", "name": "阿尔法小队 后裔", "username":"扛把子"}]},
            {"pict": [{"img": "images/timg10.jpg", "name":"死神来了 曹操", "username":"入道菊花"}]},
            {"pict": [{"img": "images/timg12.jpg", "name": "庄周", "username":"我露娜贼6"}]},
            {"pict": [{"img": "images/timg13.jpg", "name": "范海辛 李白", "username":"流线霞光"}]},
            {"pict": [{"img": "images/timg14.jpg", "name": "地狱火 孙悟空", "username":"费发你的"}]},
            {"pict": [{"img": "images/timg15.jpg", "name": "未来纪元 宫本武藏", "username":"考虑非公开是"}]},
            {"pict": [{"img": "images/timg16.jpg", "name": "龙骑士 墨子", "username":"看了模拟考"}]},
            {"pict": [{"img": "images/timg17.jpg", "name": "加勒比小姐 虞姬", "username":"会计软件"}]},
            {"pict": [{"img": "images/timg18.jpg", "name": "甄姬", "username":"开空调款"}]},
            {"pict": [{"img": "images/timg19.jpg", "name": "娜可露露", "username":"来反馈给"}]},
            {"pict": [{"img": "images/timg20.jpg", "name": "刘禅", "username":"蘑菇头"}]},
            {"pict": [{"img": "images/timg21.jpg", "name": "魔法小厨娘 安琪拉", "username":"发个人口"}]},
            {"pict": [{"img": "images/timg22.jpg", "name": "摇滚巨星 嬴政", "username":"离开他几个"}]},
            {"pict": [{"img": "images/timg23.jpg", "name": "女蜗", "username":"冷屁股来回跑"}]},
            {"pict": [{"img": "images/timg25.jpg", "name": "激情绿茵 马可波罗", "username":"来看房管局"}]},
            {"pict": [{"img": "images/timg24.jpg", "name": "末日机甲 吕布", "username":"离开家的人"}, {"img": "images/timg26.jpg", "name": "吕布", "username":"离开家的人"}]},
        ]
    }
    hero = {"play1":[],"play2":[]}
    for j in range(2):
        dist_copy = dist
        for i in range(5):
            random_index1 = random.randrange(0, len(dist_copy["image"]))
            user = dist_copy["image"][random_index1]
            random_index2 = random.randrange(0, len(user["pict"]))
            role = user["pict"][random_index2]
            hero["play{}".format(j+1)].append(role)
            del(dist_copy["image"][random_index1])
    return render(request, "myApp/work.html", hero)