from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/list.html', {'projects':projects, 'section':'project'})

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, 'projects/detail.html', {'project':project, 'section':'project'})