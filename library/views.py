from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from .forms import BookForm
from .models import Book
# Create your views here.
@login_required
def upload(request):
    context={}
    if(request.method=='POST'):
        uploaded_file=request.FILES['document']
        fs=FileSystemStorage()
        name=fs.save(uploaded_file.name,uploaded_file)
        url=fs.url(name)
        context['url']=url
    return render(request,'library/lib_upload.html',context)

def book_list(request):
    books=Book.objects.all()
    return render(request,'library/book_list.html',{'books':books})

@login_required
def upload_book(request):
    if(request.method=="POST"):
        form=BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form=BookForm()
    return render(request,'library/upload_book.html',{'form':form})

def class_library(request):
    return render(request,'library/library_prototype.html')
