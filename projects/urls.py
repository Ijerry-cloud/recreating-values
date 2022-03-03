from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('list/', views.project_list, name='list'),
    path('<int:id>/',views.project_detail, name='detail')

]