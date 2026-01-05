from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from .models import Event, Teacher
from django.utils.timezone import now
from django.core.paginator import Paginator


def home(request):
    teachers = Teacher.objects.filter(is_featured=True)[:4]
    events = Event.objects.filter(is_published=True, event_date__gte=now().date())[:4]
    return render(request, "index.html", {"events": events,  "teachers": teachers })


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

def teacher_detail(request, slug):
    teacher =Teacher.objects.get(slug=slug)
    return render(request, "teacher-single.html", {"teacher": teacher})

def support(request):
    return render(request, "support.html")

def gallery(request):
    return render(request, "gallery.html")

def event_detail(request, slug):
    event =Event.objects.get(slug=slug)
    return render(request, "event-single.html", {"event": event})

def events(request):
    event_list = Event.objects.filter(
    is_published=True,
    event_date__gte=now().date()).order_by('event_date')
    paginator = Paginator(event_list, 6)
    page_number = request.GET.get('page')
    events = paginator.get_page(page_number)

    return render(request, "events.html", {"events": events})

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

