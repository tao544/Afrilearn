from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
from .forms import ContactForm
def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")

def courses(request):
    return render(request, "courses.html")

def contact(request):
    if request.method == 'POST':
       form= ContactForm(request.POST)






       request.POST._mutable=True
       request.POST['message'] =request.POST.get('message')
       if form.is_valid():
           contact= form.save()

    return render(request, "contact.html")

def shop(request):
    return render(request, "shop.html")


def blog(request):
    return render(request, "blog.html")

def teachers(request):
    return render(request, "teachers.html")

def support(request):
    return render(request, "support.html")

def gallery(request):
    return render(request, "gallery.html")

def events(request):
    return render(request, "events.html")

