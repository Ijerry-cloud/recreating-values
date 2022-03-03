from django.shortcuts import render
from events.models import Event
from projects.models import Project

def homepage(request):
    projects = Project.objects.all()[:6]
    events = Event.objects.all()
    return render(request, 'home/landing/landing_page_main.html', {'section':'home', 'projects':projects, 'events':events })
    

def about(request):
    projects = Project.objects.all()
    events = Event.objects.all()
    return render(request, 'home/landing/about.html', {'section':'about', 'projects':projects, 'events':events})

def contact(request):
    return render(request, 'home/landing/contact.html', {'section':'contact'})

def support(request):
    return render(request, 'home/landing/support.html', {'section':'support'})


def how_to(request):
    recent_list = Event.objects.order_by('date')[:3]
    return render(request, 'home/landing/how_to.html', {'recent':recent_list, 'section':'about'})

