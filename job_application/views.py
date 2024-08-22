from django.shortcuts import render
from .forms import ApplicationForms
from .models import Form
from django.contrib import messages

def index(request):
    # this is if user presses the send/ submit button
    if request.method == "POST":
        form = ApplicationForms(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            Form.objects.create(first_name=first_name, last_name= last_name, email=email, date=date,
                               occupation=occupation)
            messages.success(request, f"{first_name}, your form was successfully submitted")

    return render(request, "index.html")
