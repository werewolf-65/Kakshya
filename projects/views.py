from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Project
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProjectForm
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (
            ListView,
            DetailView,
            CreateView,
            UpdateView,
            DeleteView,
            )
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
    return render(request,'projects/project_form.html',{'form':form})

@login_required
def star_project(request):
    pk=request.POST.get('project_id')
    project=get_object_or_404(Project,id=pk)
    is_starred=False
    if project.stars.filter(id=request.user.id).exists():
        project.stars.remove(request.user)
        is_starred=False
    else:
        project.stars.add(request.user)
        is_starred=True
    return HttpResponseRedirect(reverse('project_list'))

class ProjectUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Project
    fields=['title','description','doc','cover','link',]

    def form_valid(self,form):
        form.instance.author=self.request.user
        messages.success(self.request,f'You have edited your project details!')
        return super().form_valid(form)

    def test_func(self):
        project=self.get_object()
        if(self.request.user in project.members.all()):
            return True
        else:
            return False

class ProjectDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Project
    success_url="/"
    def test_func(self):
        project=self.get_object()
        if(self.request.user in project.members.all()):
            return True
        else:
            return False
