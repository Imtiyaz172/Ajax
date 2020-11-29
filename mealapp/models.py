from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField # < import this
from imagekit.processors import ResizeToFill # < import this
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe 
import os




class form_ajax(models.Model):
    member_name   = models.CharField(max_length=60)  
    mobile        = models.CharField(max_length=20)
    email         = models.EmailField(blank=True)
    admit_date    = models.DateField(auto_now=True)    
    status        = models.BooleanField(default=True)

    def __str__(self):
        return self.member_name

    class Meta:
        verbose_name='form_ajax'
        verbose_name_plural='form_ajax'

class advance_form_ajax(models.Model):
    member_name         = models.ForeignKey(form_ajax, on_delete=models.CASCADE,blank=True)
    member_pic        = models.ImageField(upload_to="memberpic/",blank=True)
    address       = models.TextField(max_length=200,blank=True)
    status        = models.BooleanField(default=True)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name='advance_form_ajax'
        verbose_name_plural='advance_form_ajax'



class form_ajax_table(models.Model):
    member_name   = models.CharField(max_length=60)  
    mobile        = models.CharField(max_length=20)
    email         = models.EmailField(blank=True)
    admit_date    = models.DateField(auto_now=True)    
    status        = models.BooleanField(default=True)

    def __str__(self):
        return self.member_name

    class Meta:
        verbose_name='form_ajax_table'
        verbose_name_plural='form_ajax_table'

class advance_form_ajax_table(models.Model):
    member_name         = models.ForeignKey(form_ajax, on_delete=models.CASCADE,blank=True)
    member_pic        = models.ImageField(upload_to="memberpic/",blank=True)
    address       = models.TextField(max_length=200,blank=True)
    status        = models.BooleanField(default=True)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name='advance_form_ajax_table'
        verbose_name_plural='advance_form_ajax_table'

































