from django.shortcuts import render
from . models import ContactInfo
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.


def contact(request):
    myObject = ContactInfo.objects.get()
    if request.method == "POST":
        mySubject = request.POST['subject']
        myEmail   = request.POST['email']
        myMessage = request.POST['message']

        send_mail(
            mySubject,
            myMessage,
            myEmail,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        
    context = {
        'myObject' : myObject
    }
    return render(request, 'pages/contact.html', context)