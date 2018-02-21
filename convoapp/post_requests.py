#to get started run this file (python post_requests.py)

import requests

post_request = requests.session()
post_request.get('http://127.0.0.1:8000/message/')
csrftoken = post_request.cookies['csrftoken']

charles_data = {'name': 'charles', 'conversation_id': '1', 'message_body': 'I am Charles','csrfmiddlewaretoken' : csrftoken}
jeff_data = {'name': 'Jeff', 'conversation_id': '2', 'message_body': 'I am Jeff','csrfmiddlewaretoken' : csrftoken}
amanda_data = {'name': 'Amanda', 'conversation_id': '2', 'message_body': 'I am Amanda','csrfmiddlewaretoken' : csrftoken}

post_request.post('http://127.0.0.1:8000/message/', data=charles_data, cookies=post_request.cookies)
post_request.post('http://127.0.0.1:8000/message/', data=jeff_data, cookies=post_request.cookies)
post_request.post('http://127.0.0.1:8000/message/', data=amanda_data, cookies=post_request.cookies)
