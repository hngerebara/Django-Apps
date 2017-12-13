# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    # author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    upload_file = models.FileField(null=True, blank=True)
    published_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_date = models.DateField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        ordering =['-published_date']
    #
    # def get_absolute_url(self):
    #     return reverse("detail", kwargs={"id": self.id})