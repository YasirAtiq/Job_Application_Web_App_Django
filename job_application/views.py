from django.shortcuts import render
from .forms import ApplicationForm
from .models import DataBase

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
    return render(request, "index.html")
