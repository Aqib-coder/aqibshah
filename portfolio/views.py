from django.http import HttpResponse
from django.shortcuts import render
from services.models import Service
from my_projects.models import Project
from clients.models import Client

def index(request):
    services = Service.objects.all()
    projects = Project.objects.all()
    data = {
        "services":services,
        "projects":projects,
        "error":False
    }

    if request.method == 'POST':
        print(request.POST.get("c_name"))

        if request.POST.get("c_name") == "" or request.POST.get("c_email") == "" or request.POST.get("work") == "" or request.POST.get("c_phone") == "":
            data = {
                "services":services,
                "projects":projects,
                "error":True
            }
            return render(request,"index.html",data)
        
        print(request.POST.get("c_name"))
        client=Client(client_name = request.POST.get("c_name"),
                      client_phone = request.POST.get("c_phone"),
                      client_email = request.POST.get("c_email"),
                      client_work = request.POST.get("work"))
        client.save()
        
    return render(request,"index.html",data)



def project(request,slug):
    project = Project.objects.get(project_slug = slug)
    return render(request,"project.html",{"project":project})