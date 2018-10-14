from django.conf.urls import url
import django_twilio
from .views import home,sms

urlpatterns = [
     url(r'^api/$', home),
     url(r'^send/', sms),
]