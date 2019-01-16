from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
#Dummy Data
# posts=[
#     {
#     'author':'Subodh',
#     'title':'Blog Post 1',
#     'content':'First post in this site',
#     'date_posted':'November 28,2018',
#     },
#     {
#     'author':'Mandeep',
#     'title':'Blog Post 2',
#     'content':'Second post in this site',
#     'date_posted':'November 29,2018',
#     },
# ]
def home(request):
    context={'posts':Post.objects.all()}
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title' :'About'})
