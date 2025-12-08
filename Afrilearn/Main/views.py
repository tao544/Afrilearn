from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")

def courses(request):
    return render(request, "courses.html")

def contact(request):
    message_sent =False
    form=ContactForm()
    if request.method == 'POST':
       
        form= ContactForm(request.POST)


        if form.is_valid():
           contact= form.save()




           send_mail(
               subject = f"New Contact Form: {contact.subject}",
               message = f"""
            Name: {contact.name}
            Email:{contact.email}
            Phone: {contact.phone}
            Message:
            {contact.message}

            """,

                from_email ="Afrilearn contact form <no-reply@gmail.com>",
                recipient_list=["adeedraiment@gmail.com", ],
                fail_silently=False
           )


        message_sent=True
        form =ContactForm()

    return render(request, "contact.html", {"form": form, "message_sent": message_sent})

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

def documentation(request):
    return render(request, "documentation.html")

def policy(request):
    return render(request, "policy.html")

def privacy(request):
    return render(request, "privacy.html")

def faqs(request):
    return render(request, "faqs.html")

def support(request):
    return render(request, "support.html")

