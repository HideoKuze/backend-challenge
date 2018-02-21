# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms
from models import InputInfo

class InputInfoForm(forms.ModelForm):

	class Meta:
		model = InputInfo
		fields = ['name', 'conversation_id', 'message_body']