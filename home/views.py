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
    contents =fromEmail+'to depromeet :  '+message
 	toEmail = 'deproapply@gmail.com'
	email = EmailMessage('questions from '+ name, message, fromEmail, to=[toEmail])
    email.send()
    return HttpResponseRedirect(reverse('home'))

