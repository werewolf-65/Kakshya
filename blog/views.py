from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CommentForm
from .models import Post,Comment
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (
            ListView,
            DetailView,
            CreateView,
            UpdateView,
            DeleteView,
            )
from django.core.paginator import Paginator
from django.urls import reverse
# Create your views here.
def home(request):
    context={'posts':Post.objects.all()}
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title' :'About'})

class PostListView(ListView):
    model=Post
    template_name='blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name='posts'
    ordering=['-date_posted']
    paginate_by=6

class UserPostListView(ListView):
    model=Post
    template_name='blog/user_posts.html' #<app>/<model>_<viewtype>.html
    context_object_name='posts'
    # ordering=['-date_posted']
    paginate_by=6

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model=Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content','img']

    def form_valid(self,form):
        form.instance.author=self.request.user
        messages.success(self.request,f'You have created a new post!')
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content','img']

    def form_valid(self,form):
        form.instance.author=self.request.user
        messages.success(self.request,f'You have edited your post!')
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if(self.request.user==post.author):
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url="/"
    def test_func(self):
        post=self.get_object()
        if(self.request.user==post.author):
            return True
        else:
            return False
def post_list(request):
    post_list=Post.objects.all()
    paginator=Paginator(post_list,5)
    page=request.GET.get('page')
    posts=paginator.get_page(page)

    context={
        'posts':posts,

    }
    return render(request,'blog/home.html',context)

def post_detail(request,pk):
    post=Post.objects.get(id=pk)
    comments=Comment.objects.filter(post=post).order_by('-id')
    is_upvoted=False
    if post.upvotes.filter(id=request.user.id).exists():
        is_upvoted=True
    if request.method=='POST':
        comment_form=CommentForm(request.POST or None)
        if comment_form.is_valid():
            content=request.POST.get('content')
            comment=Comment.objects.create(post=post,user=request.user,content=content)
            comment.save()
            #return HttpResponseRedirect(post.get_absolute_url())
            return HttpResponseRedirect(reverse('post-detail', args=(pk, )))
    else:
        comment_form=CommentForm()
    context={
        'post':post,
        'is_upvoted':is_upvoted,
        'total_upvotes':post.total_upvotes(),
        'comments':comments,
        'comment_form':comment_form,
    }
    return render(request,'blog/post_detail.html',context)
def upvote_post(request):
    pk=request.POST.get('post_id')
    post=get_object_or_404(Post,id=pk)
    is_upvoted=False
    if post.upvotes.filter(id=request.user.id).exists():
        post.upvotes.remove(request.user)
        is_upvoted=False
    else:
        post.upvotes.add(request.user)
        is_upvoted=True
    return HttpResponseRedirect(reverse('post-detail', args=(pk, )))

def gallery(request):
    post_list=Post.objects.all()
    paginator=Paginator(post_list,6)
    page=request.GET.get('page')
    posts=paginator.get_page(page)

    context={
        'posts':posts,

    }
    return render(request,'blog/gallery.html',context)
