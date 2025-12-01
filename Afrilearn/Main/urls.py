
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('courses/', views.courses, name="courses"),
    path('contact/', views.contact, name="contact"),
    path('shop/', views.shop, name="shop"),
    path('gallery/', views.gallery, name="gallery"),
    path('blog/', views.blog, name="blog"),
    path('teachers/', views.teachers, name="teachers"),
    path('support/', views.support, name="support"),   
    path('events/', views.events, name="events"),   
]
