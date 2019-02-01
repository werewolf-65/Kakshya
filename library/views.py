from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# Create your views here.
def upload(request):
    context={}
    if(request.method=='POST'):
        uploaded_file=request.FILES['document']
        fs=FileSystemStorage()
        name=fs.save(uploaded_file.name,uploaded_file)
        url=fs.url(name)
        context['url']=url
    return render(request,'library/lib_upload.html',context)
