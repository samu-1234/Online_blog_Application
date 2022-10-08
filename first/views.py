from colorsys import TWO_THIRD
from email.mime import image
import imp
from importlib import import_module
from pyexpat.errors import messages
from turtle import pos
from unicodedata import name
from urllib import response
# from blogsystem.first.models import BlogInfo
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from first.models import Reg,Login,BlogInfo,Comment
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import BlogInfo
from .form import BlogForm
# Create your views here.


def index(request):
    return render(request, 'index.html') 

def blog_detail(request,id):
    bdata=BlogInfo.objects.get(id=id)
    com=Comment.objects.all()
    # print(bdata)
    return render(request,'blog_detail.html',{'bdata': bdata,'com':com})

def blog_detailstype(request,id):
   return redirect('/blog_detail')

def showdata(request):
    data = BlogInfo.objects.all()
    return render(request,"showdata.html",{'data':data})

def showdatainlogin(request):
    data = BlogInfo.objects.all()
    return render(request,"showdata.html",{'data':data})
    
def signup(request):
    return render(request, 'signup.html')

def technology(request):
    data = BlogInfo.objects.filter(post_type="technology")
    return render (request, 'technology.html',{'data':data})

def technologyinlogin(request):
    return redirect('/technology')

def socialmedia(request):
    data = BlogInfo.objects.filter(post_type="social media")
    return render (request, 'social media.html',{'data':data})

def socialmediainlogin(request):
    return redirect('/social media')

def onlinemareting(request):
    data = BlogInfo.objects.filter(post_type="Online marketing")
    return render (request, 'online marketing.html',{'data':data})

def onlinemaretinginlogin(request):
    return redirect('/online marketing')

def writting(request):
    data = BlogInfo.objects.filter(post_type="writting")
    return render (request, 'writting.html',{'data':data})

def writtinginlogin(request):       
    return redirect('/writting')

#make change by samruddhi
def saveRegister(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        pass1=request.POST.get("pass1")
        re_pass=request.POST.get("re_pass")
        en=Reg(name=name,email=email,pass1=pass1,re_pass=re_pass)
        en.save()
    return render(request, 'signup.html')




def login(request):
    return render(request, 'login.html')

def savelogin(request):
    if request.method=="POST":
        isLoginSuccessful = None
        # user=Reg.objects.all()
        name=request.POST.get("your_name")
        pass1=request.POST.get("your_pass")
        # # en1=Login(your_name=name,your_pass=pass1)
        # # en1.save()
        obj = Reg.objects.filter(name=name, pass1=pass1 )
        if obj :
            isLoginSuccessful = True
        else:
            isLoginSuccessful = False
    
    return render(request, 'after_login.html   ', {"isLoginSuccessful": isLoginSuccessful})

def check(request):
    if(name.login==name.register):
        return render(request,"Login succesfull")  
    else :
        return render(request,"Login unsuccesfull")

def load_form(request):
    context = {'form' : BlogForm}
    try:
        if request.method=="POST":
            form = BlogForm(request.POST)
            image = request.FILES['image']
            title =request.POST.get('title')
            description=request.POST['description']
            # user=request.user

            if form.is_valid():
                content = form.cleaned_data['content']
            
            
            BlogInfo.objects.create(
                # user=user,
                title=title,
                description=description,image=image,
                content=content   
            )
            
            return redirect(savelogin)
            # return redirect(start)
            # return render(request,'home.html',{'title':vtitle,'description':vdescription})
       
    except Exception as e:
        print(e)
    
    return render(request,'form.html',context)


def saveform(request):
    
    if request.method=="POST":
        image=request.POST.get('image')
        title=request.POST.get('title')
        description=request.POST.get('description')
        post_type=request.POST.get('post_type')
        data=BlogInfo(image=image,title=title,description=description,post_type=post_type)
        data.save()
    return render(request,'home.html')

def register(request):
    
    if request.method == 'POST':
        isRegistrationSuccessful =False
        flag = True
        username = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['re_pass']

        # 2 may check for arrorneous inputs
        if len(username)>50:
            messages.error(request,"username must be under must be under 10 characters")
            flag = False
            # return redirect('login')
            
        # 2 may 
        if not username.isalnum():
            messages.error(request,"username should only contaion letters and numbers")
            flag = False
            # return redirect('login')
       
        if pass1 != pass2:
            messages.error(request,"password do not match")
            flag = False
            # return redirect('login')

        if flag:
            en=Reg(name=username,email=email,pass1=pass1,re_pass=pass2)
            en.save()
            isRegistrationSuccessful = True

    return render(request, 'signup.html', {"isRegistrationSuccessful": isRegistrationSuccessful})

def blogs_comments(request):
    if request.method=="POST":
        content=request.POST.get('content')
        # title=request.POST.get('title')
        data=Comment(content=content)
        data.save()
    return redirect(showdata)
    
def logout(request):
    return redirect(index)


    
        


