from django.shortcuts import render

# Create your views here.
def home(request):
    thispage = "home page"
    return render(request, "home.html", {"name": thispage})


def about(request):
    thispage = "about page"
    return render(request, "about.html", {"name": thispage})
