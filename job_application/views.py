from django.shortcuts import render
from .forms import ApplicationForm
from .models import DataBase
from django.contrib import messages
from django.core.mail import EmailMessage

def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first name"]
            last_name = form.cleaned_data["last name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["doj"]
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
