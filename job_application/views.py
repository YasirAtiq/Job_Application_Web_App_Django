from django.shortcuts import render, get_object_or_404
from .forms import ApplicationForm
from .models import DataBase
from django.contrib import messages
from django.core.mail import EmailMessage
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

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
@receiver(post_save, sender=DataBase)
def send_interview_date_change(sender, instance, created, **kwargs):
    if not created:
        if instance._state.db or (hasattr(instance, 'user') and instance.user and instance.user.is_staff):
            message = f"""Dear {str(instance)},
We have changed the date of our interview to {instance.date}. We are sorry
for this change, if you have any queries or any difficulties to join,
please reply to this email. Note that we may take from 2 to 3 business days to reply back.
The Hiring Team."""
            to_email = instance.email
            email_message = EmailMessage("Interview Date Updated", message, to=[to_email])
            email_message.send()

@receiver(post_delete, sender=DataBase)
def send_email_when_interview_cancelled(sender, instance, **kwargs):
    message = f"""Dear {str(instance)},
We are very sorry to inform you that we have cancelled your interview. If you think this is a mistake
then please reply here. Note that we may take 2 to 3 days to reply back.
The Hiring Team."""
    to_email = instance.email
    email_message = EmailMessage("Interview Cancelled", message, to=[to_email])
    email_message.send()