from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Event

def event_list(request):
    object_list = Event.objects.order_by('-date')
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