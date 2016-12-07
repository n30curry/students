from django.conf.urls import *
from zixu.views import *

urlpatterns = patterns('',
        url(r'^zixun1/(\d*)',zixu),
        url(r'^zixun2/',zixun1),
        url(r'^login/',login),
        url(r'^index',index),
        url(r'^denglu',denglu),
        url(r'^zhuce',zhuce),
        )
