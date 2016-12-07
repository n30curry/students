from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Stu_message(models.Model):
    name = models.CharField(max_length = 30)
    phone = models.CharField(max_length = 30)
    zhuangye = models.CharField(max_length = 50)

    def __unicode__(self):
        return '%s %s %s'%(self.name,self.phone,self.zhuanye)

class user(models.Model):
    name = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)
    email = models.EmailField()
