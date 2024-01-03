from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Event

def events_preview(request): #This and events_preview2 should be the correct representation of an event. the rest functions here are supposed to be for articles as i made a mistake in making a models instance of event to represent an article instead
    recent_list = Event.objects.order_by('-date')[:3]
    return render(request, 'events/preview.html', {'recent':recent_list, 'section':'events'})

def events_preview2(request):
    recent_list = Event.objects.order_by('-date')[:3]
    return render(request, 'events/preview2.html', {'recent':recent_list, 'section':'events'})



def event_list(request):
    object_list = Event.objects.all()
    recent_list = Event.objects.order_by('-date')[:3]
    paginator = Paginator(object_list, 5)
    page = request.GET.get('page')
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        #return the first page if page is not an integer
        events = paginator.page(1)
    except EmptyPage:
        # return the last page if page is out of range
        events = paginator.page(paginator.num_pages)
    return render(request, 'events/list.html', {'events':events, 'page':page, 'recent':recent_list, 'section':'articles'})
def event_list_by_category(request, subject):
    obj_list = Event.objects.filter(category__subject__iexact=subject)
    recent_list = Event.objects.order_by('-date')[:3]
    paginator = Paginator(obj_list, 5)
    page = request.GET.get('page')
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        #return the first page if page is not an integer
        events = paginator.page(1)
    except EmptyPage:
        # return the last page if page is out of range
        events = paginator.page(paginator.num_pages)
    return render(request, 'events/list.html', {'events':events, 'page':page, 'recent':recent_list, 'section':'articles'})

def event_list_by_date(request, year, month):
    obj_list = Event.objects.filter(date__year=year, date__month=month)
    recent_list = Event.objects.order_by('-date')[:3]
    paginator = Paginator(obj_list, 5)
    page = request.GET.get('page')
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        #return the first page if page is not an integer
        events = paginator.page(1)
    except EmptyPage:
        # return the last page if page is out of range
        events = paginator.page(paginator.num_pages)
    return render(request, 'events/list.html', {'events':events, 'page':page, 'recent':recent_list, 'section':'articles'})

def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    recent_list = Event.objects.order_by('-date').exclude(id=event.id)[:3]
    return render(request, 'events/detail.html', {'event':event, 'recent':recent_list, 'section':'articles'})