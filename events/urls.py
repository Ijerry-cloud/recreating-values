from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('list/', views.event_list, name='list'),
    path('detail/<int:id>/', views.event_detail, name='detail'),
    path('<str:subject>/', views.event_list_by_category),
    path('<int:year>/<str:month>/', views.event_list_by_date),
    path('<int:id>/', views.event_detail)
]