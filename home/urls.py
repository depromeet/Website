from django.conf.urls import url
from . import views
from .views import home, mail

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^send_mail$', mail, name="sendMail"),
]