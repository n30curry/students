#!/usr/bin/python
#coding=utf-8

from django.shortcuts import render,render_to_response
from zixu import models
from django.http import HttpResponse,HttpResponseRedirect
from zixu import forms
from django.utils.safestring import mark_safe
# Create your views here.

def zixu(request,page1):
    # del request.session["user"]
    user = request.session.get("user")
    try:
        per_item = int(page1)
    except Exception,e:
        per_item = 1

    if user:
        # const = 5
        # if const/2 < per_item


        stu_list = models.Stu_message.objects.all()[(per_item - 1)*2:per_item*2]
        count = models.Stu_message.objects.all().count()

        page_items = divmod(count,2)
        if page_items[1] == 0:
            page = page_items[0]
        else:
            page = page_items[0] + 1

        ll = []
        if per_item <= 1:
            prv_html = '<a href="/zixun/zixun1/#">上一页</a>'
        else:
            prv_html = '<a href="/zixun/zixun1/%d">上一页</a>'%(per_item-1)

        ll.append(prv_html)

        begin = per_item - 4
        end = per_item + 3

        if page < 7:
            begin = 0
            end = page
        else:
            if per_item < 4:
                begin = 0
                end = 7
            else:
                if per_item + 4 > page:
                    begin = page - 4
                    end = page
                else:
                    begin = per_item -4
                    end = per_item + 3
            # end = count
        for i in range(begin,end):
            if per_item == i + 1:
                ahtml = '<a style = "color:red;border:1px solid red" href="/zixun/zixun1/%d" >%d</a>'%(i+1,i+1)
            else:
                ahtml = '<a href="/zixun/zixun1/%d">%d</a>'%(i+1,i+1)
            ll.append(ahtml)
        if per_item < page:
            next_html = '<a href="/zixun/zixun1/%d">下一页</a>'%(per_item+1,)
        else:
            next_html = '<a href="/zixun/zixun1/%d">下一页</a>'%(page)

        ll.append(next_html)

        pages = ''.join(ll)
        pa = mark_safe(pages)
        # page = mark_safe('<a href="/zixun/zixun1/2">2</a>')
        return render_to_response('show.html',{'stu_list':stu_list,'user':user,'page':pa,'per':per_item})
    else:
        return render_to_response("index.html")


def zixun1(request):
    # per_item = int(page)
    user = request.session.get("user")
    if request.POST['name'] and request.POST['phone'] and request.POST['zhuanye']:
        name1 = request.POST['name']
        phone1 = request.POST['phone']
        zhuanye1 = request.POST['zhuanye']
        p1 = models.Stu_message(name = name1,phone = phone1,zhuangye = zhuanye1)
        p1.save()


        # stu_list = models.Stu_message.objects.all()[(per_item - 1)*5:per_item*5]
        stu_list = models.Stu_message.objects.all()[0:5]
        count = models.Stu_message.objects.all()[0:5].count()
        # return render_to_response('show.html',{'stu_list':stu_list,'user':user})
        return HttpResponseRedirect('/zixun/zixun1/')
        #return HttpResponse('ok')
    else:
        return render_to_response("show.html",{'user':user})


def login(request):
    ret = {"data":None,"error":""}
    # ret["data"] = obj
    checkform = forms.ALogin(request.POST)
    checkresult = checkform.is_valid()
    if checkresult:
        name = request.POST.get("name")
        print name
        email = request.POST.get("email")
        pwd = request.POST.get("password")
        p1 = models.user(name = name,email = email, password = pwd)
        p1.save()
        return HttpResponse("ok!!!")
    else:
        formerrors = checkform.errors
        firsterrors = checkform.errors.as_data().values()[0][0].messages[0]
        ret["error"] = firsterrors
        return render_to_response("login.html",{"data":formerrors})


def index(request):
    return render_to_response("index.html")


def denglu(request):
    if request.method == "GET":
        names = request.GET.get("name")
        pwd = request.GET.get("password")
        try:
            obj = models.user.objects.get(name = names,password = pwd)
        except Exception,e:
            obj = None
            data = '用户名或密码不存在请重新登陆'
        if obj:
            request.session['user'] = names
            return HttpResponse("denglu ok!!!")
        else:
            return render_to_response('index.html',{'data':data})
    else:
        return render_to_response('index.html')

def zhuce(request):
    return render_to_response('login.html')
