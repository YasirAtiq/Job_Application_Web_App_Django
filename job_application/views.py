from django.shortcuts import render, get_object_or_404
from .forms import ApplicationForm
from .models import DataBase
from django.contrib import messages
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.conf import settings

def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]
            DataBase.objects.create(first_name=first_name, 
                                    last_name=last_name, email=email, 
                                    date=date, occupation=occupation)
            messages.success(request, "Form Submitted Successfuly!")

            content = f"""
Dear {first_name + " " + last_name},
We have recieved your application to join our team. 
Please come to our interview at {str(date)[:10]}.
Here are your details:
First Name: {first_name}
Last Name: {last_name}
Email: {email}
Current Occupation: {occupation}.
With Regards,
The hiring team"""
            
            email_message = EmailMessage("Application Form Submitted!", content, to=[email])
            email_message.send()
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")
<<<<<<< HEAD

@receiver(post_save, sender=DataBase)
def send_interview_date_change(sender, instance, created, **kwargs):
    if not created:
        if instance._state.db or (hasattr(instance, 'user') and instance.user and instance.user.is_staff):
            subject = 'Interview Date Updated'
            message = f"""Dear {str(instance)},
We have changed the date of our interview to {instance.date}. We are sorry
for this change, if you have any queries or any difficulties to join,
please reply to this email. Note that we may take from 2 to 3 business days to reply back.
The Hiring Team."""
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = instance.email
            send_mail(subject, message, from_email, [to_email])
=======
>>>>>>> 0f01bc12a80e76968822ae6b6bd01c8425afdbec
