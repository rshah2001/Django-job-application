from django.shortcuts import render
from .forms import ApplicationForms


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
            print(first_name)

    return render(request, "index.html")
