#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse

def zixu(request):
    return HttpResponse("hello world")

