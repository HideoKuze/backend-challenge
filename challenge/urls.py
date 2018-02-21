from django.conf.urls import url
from django.contrib import admin
from convoapp import views
from convoapp.views import conversationview
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^conversations/(?P<convo_identification>\d+)', views.conversationview, name='conversationview'),
    url(r'^message/', views.add_message, name='message'),
]
