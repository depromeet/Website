# -*- coding: utf-8 -*- 
from django.shortcuts import render
from django.utils import timezone
from django.core.urlresolvers import reverse

from django.http import HttpResponse, HttpResponseRedirect
from .models import Activity
from django.core.mail import EmailMessage, send_mail

def home(request):
    activities = Activity.objects.all()
    return render(request, 'home/index.html', {'activities': activities})

def mail(request):
    name= request.POST['name']
    fromEmail= request.POST['email']
    message= request.POST['message']
    toEmail = 'deproapply@gmail.com'
    email = EmailMessage(name+'님이 보내주신 메일입니다.'.decode('utf-8'), message+'\n\n'+'sent from depromeet.com :-)'.decode('utf-8'), fromEmail, to=[toEmail])
    email.send()
    return HttpResponseRedirect(reverse('home'))