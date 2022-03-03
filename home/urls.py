from django.urls import path
from . import views 

app_name = 'home'

urlpatterns=[
    path('about/', views.about, name='about'),
    path('how_to/', views.how_to, name='how_to'),
    path('contact/', views.contact, name='contact'),
    path('support/', views.support, name='support'),
    path('', views.homepage, name='homepage'),
]