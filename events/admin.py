from django.contrib import admin
from .models import Category, Event
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['subject']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'date',]