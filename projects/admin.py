from django.contrib import admin
from .models import ProjectCategory, Project
# Register your models here.

@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ['subject']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'estimate_cost', 'commencement_date', 'completed']
    exclude = ('image1_64', 'image2_64', 'image3_64')