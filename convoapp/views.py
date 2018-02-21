from __future__ import unicode_literals
from django.http import HttpResponse
from .models import InputInfo
from forms import InputInfoForm
import json
from django.shortcuts import render

#this view will return a certain conversations messages by accepting an argument 
def conversationview(request, convo_identification):
	data = InputInfo.objects.all()
	conversation_identification = convo_identification
	header = {'conversation_id': '', 'messages': []}
	entry = {}
	output = {}

	for i in data:
		if i.conversation_id == conversation_identification:
			header['conversation_id'] = i.conversation_id
			entry = {}
			entry['message_body'] = i.message_body
			entry['date_created'] = str(i.created)
			entry['sender'] = i.name	
			header.get('messages').append(entry)
			output = json.dumps(header, indent=4)

	#if the conversation does not exist return a 404 error
	if InputInfo.objects.filter(conversation_id=convo_identification).exists() == False:
		return HttpResponse(status=404)

	#make sure to specify content_type parameter
	return HttpResponse(output, content_type='application/javascript; charset=utf8') 

# Was going to use @csrf_exempt originally because there was no template containing a view, but it's more secure to just csrf with a dummy template
def add_message(request):
	fields = ['name', 'conversation_id', 'message_body']
	if request.method == 'POST':
		form = InputInfoForm(request.POST)
		#validate/ DB won't update if form is invalid
		if form.is_valid():
			InputInfo.name = request.POST.get('name')
			InputInfo.conversation_id = request.POST.get('conversation_id')
			InputInfo.message_body = request.POST.get('message_body')
			form.save()

		else:
			form = InputInfoForm(request.POST)

	return render(request, 'blank.html')