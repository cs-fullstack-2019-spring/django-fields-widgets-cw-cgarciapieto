from django.shortcuts import render
from .models import HeroAppModel
from .forms import heroForm


# Create your views here.
# renders the index page where there is a link to apply
def index(request):
    return render(request, 'heroApp/index.html')

# renders the application page
def application(request):
    return render(request, 'heroApp/application.html')

# renders the form and allows user apply
def newform(request):
    newForm = heroForm()

    context = {
        "newForm": newForm
    }

    return render(request, "heroApp/thankyou.html", context)

# renders html page
def welcome(request):
    return render(request, "heroApp/thankyou.html")
