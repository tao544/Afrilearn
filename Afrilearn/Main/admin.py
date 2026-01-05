from django.contrib import admin
from .models import Contact, Event, Teacher

# Register your models here.

admin.site.register(Contact)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display=("title", "event_date", "location", "is_published")
    list_filter=("event_date", "is_published")
    search_fields= ("title", "location")
    prepopulated_fields= {"slug": ("title",)}


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display= ("name", "title", "is_featured")
    prepopulated_fields = {"slug": ("name",)} 
    list_filter = ("is_featured",)
    search_fields =("name", "title")  
     
