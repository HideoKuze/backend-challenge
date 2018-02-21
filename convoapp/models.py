# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class InputInfo(models.Model):
	name = models.CharField(max_length=10, blank=False)
	conversation_id = models.CharField(max_length=4, blank=False)
	message_body = models.TextField(blank=False)
	created = models.DateTimeField(default=timezone.now)
	#this is for using datetime.date.today() in tasks.py
	date_without_time = models.DateField(default=timezone.now)
