from django.shortcuts import render
from . import models
# Create your views here.
def home(request):
    data=models.Exam.objects.order_by('-id')[:3]
    if request.method=='POST':
        email=request.POST.get('email')
        s=models.newsletter(email=email)
        s.save()
    context={
        'data':data,
    }
    return render(request,'Education/index.html',context)
def about(request):
    return render(request,'Education/about.html')
def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phno=request.POST.get('phno')
        msg=request.POST.get('msg')
        c=models.contact(name=name,email=email,phno=phno,msg=msg)
        c.save()
    return render(request,'Education/contact.html')
def courses(request):
    data=models.Exam.objects.all()
    context={
        'data':data,
    }
    return render(request,'Education/courses.html',context)
def archive(request,pk):
    exam=models.Exam.objects.get(pk=pk)
    rounds=models.Round.objects.filter(exam=exam)
    context={
        'rounds':rounds,
        'exam':exam,
    }
    return render(request,'Education/archive.html',context)

def blogs(request,pk):
    rounds=models.Round.objects.get(pk=pk)
    blogs=models.Blog.objects.filter(rounds=rounds)
    context={
        'blogs':blogs,
        'name':rounds,
    }
    return render(request,'Education/blog.html',context)

def view(request,pk):
    data=models.Blog.objects.get(pk=pk)
    context={
        'data':data,
    }
    return render(request,'Education/viewblog.html',context)
# ######################################################################**********************

def downloads(request):
    data=models.StudyMaterial.objects.all()
    context={
        'data':data
    }
    return render (request,'Education/download.html',context)