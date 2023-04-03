from django.shortcuts import render
from .forms import RegisterForm,movie,tvshow
from .models import movies,tvshows
from django.urls import reverse
from django.contrib.auth import authenticate, login as LOGIN,logout as LOGOUT
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def register(request):
    registration = False
    if request.method == 'POST':
        store = RegisterForm(request.POST)
        if store.is_valid():
            v =store.save()
            v.set_password(v.password)
            v.save()
            registration =True
    else:
        store = RegisterForm()
        print(RegisterForm())
    return render(request,'register.html',{'form':store,"registration":registration})

def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(username=name,password=password)
        if user:
            LOGIN(request,user)
            return HttpResponseRedirect(reverse('app:addmovies'))
        else:
            return HttpResponse("<h1 style='color:blue;'>entered credentials are incorrect</h1>")
    else:
        return render(request,"login.html")
        
def logout(request):
    LOGOUT(request)
    return HttpResponseRedirect(reverse('app:movies'))

def addmovies(request):
    show = False
    if request.method == 'POST':
        f = movie(request.POST,request.FILES)
        if f.is_valid():
            f.save()
            show = True
            return render(request,'addmovies.html',{"show":show})
            
        return HttpResponseRedirect(reverse('app:movies'))
            
    else:
        f = movie()
        print(f)
        return render(request,"addmovies.html",{'form':f})

def addtvshows(request):
    show = False
    if request.method == 'POST':
        f = tvshow(request.POST,request.FILES)
        if f.is_valid():
            f.save()
            show = True
            return render(request,'addtvshows.html',{"show":show})

            
        return HttpResponseRedirect(reverse('app:tvshows'))
            
    else:
        f = tvshow()
        print(f)
        return render(request,"addtvshows.html",{'form':f})
    

def moviess(request):
    details = movies.objects.all()    
    return render(request,"movies.html",{'details':details})

def tvshowss(request):
    details = tvshows.objects.all()    
    return render(request,"tv shows.html",{'details':details})






