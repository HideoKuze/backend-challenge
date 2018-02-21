#unittest code
import requests
from django.test import TestCase
from convoapp.models import InputInfo
from django.urls import reverse
import sqlite3


class InputInfoTestCase(TestCase):	

	def setUp(self):
		post_request = requests.session()
		post_request.get('http://127.0.0.1:8000/message/')
		csrftoken = post_request.cookies['csrftoken']

		luke_data = {'name': 'Luke', 'conversation_id': '1', 'message_body': 'I am a Jedi, like my father before me','csrfmiddlewaretoken' : csrftoken}
		vader_data = {'name': 'Vader', 'message_body': 'No, I am your father','csrfmiddlewaretoken' : csrftoken}
		leia_data = {'name': 'Leia', 'conversation_id': 2, 'message_body': 'You are short','csrfmiddlewaretoken' : csrftoken}
		lando_data = {'name': 'Lando', 'conversation_id': '12345', 'message_body': 'This is getting worse al the time','csrfmiddlewaretoken' : csrftoken}

		#POST the Luke data
		post_request.post('http://127.0.0.1:8000/message/', data=luke_data, cookies=post_request.cookies)
		#POST the Vader data
		post_request.post('http://127.0.0.1:8000/message/', data=vader_data, cookies=post_request.cookies)
		#POST the Leia data
		post_request.post('http://127.0.0.1:8000/message/', data=leia_data, cookies=post_request.cookies)
		#POST the Lando data
		post_request.post('http://127.0.0.1:8000/message/', data=lando_data, cookies=post_request.cookies)

	def test_for_valid_entries(self):
		#connect to database
		conn = sqlite3.connect('db.sqlite3')
		c = conn.cursor()
		c.execute("SELECT * FROM convoapp_inputinfo WHERE name='Luke'")
		luke = c.fetchone()
		#determine if entry is there
		self.assertTrue(luke)

	def test_for_missing_id(self):
		conn = sqlite3.connect('db.sqlite3')
		c = conn.cursor()
		c.execute("SELECT * FROM convoapp_inputinfo WHERE name='Vader'")
		vader = c.fetchone()

		self.assertFalse(vader)

		#test will work no matter what because CharField entries are always strings
	def test_for_integer_input(self):
		conn = sqlite3.connect('db.sqlite3')
		c = conn.cursor()
		c.execute("SELECT * FROM convoapp_inputinfo WHERE name='Leia'")
		leia = c.fetchone()

		self.assertTrue(leia)

	def test_for_long_id(self):
		#will test for ID that is long than 4 digits
		conn = sqlite3.connect('db.sqlite3')
		c = conn.cursor()
		c.execute("SELECT * FROM convoapp_inputinfo WHERE name='Lando'")
		Lando = c.fetchone()

		self.assertFalse(Lando)
