
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
    path('documentation/', views.documentation, name="documentation"),   
    path('faqs/', views.faqs, name="faqs"),   
    path('policy/', views.policy, name="policy"),   
    path('privacy/', views.privacy, name="privacy"),   
    path('support/', views.support, name="support"),   
]
