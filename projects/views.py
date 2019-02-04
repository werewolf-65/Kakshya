from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Project
from .forms import ProjectForm
# Create your views here.
def project_list(request):
    projects=Project.objects.all()

    return render(request,'projects/project_list.html',{'projects':projects})

def upload_project(request):
    if(request.method=="POST"):
        form=ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form=ProjectForm()
    return render(request,'projects/upload_project.html',{'form':form})

def star_project(request):
    pk=request.POST.get('post_id')
    project=get_object_or_404(Project,id=pk)
    is_starred=False
    if project.stars.filter(id=request.user.id).exists():
        project.stars.remove(request.user)
        is_starred=False
    else:
        project.stars.add(request.user)
        is_starred=True
    return HttpResponseRedirect(reverse('project_list'))
