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
    contents = 'email from '+name+' whose email: '+fromEmail+'to depromeet :  '+message
    toEmail = 'elvmaks@gmail.com'

    email = EmailMessage('mail from depromeet site', contents, to=[toEmail])
    email.send()
    return HttpResponseRedirect(reverse('home'))

