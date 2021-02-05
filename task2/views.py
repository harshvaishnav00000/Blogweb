from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as Login
from django.contrib.auth import logout as Logout
from django.contrib.auth.models import User
import random
from django.contrib import messages
from .models import post
from django.core.files.storage import FileSystemStorage

c = 0

def login(request):
    return render(request, 'login.html')

def logout(request):
    Logout(request)
    return redirect('/')

def signup(request):
    a = random.randint(0,100)
    b = random.randint(0,100)
    global c
    c = a + b
    return render(request, 'signup.html', {'a': a, 'b': b})

def handlelogin(request):
    username = request.POST['username']
    password=request.POST['password']
    user=authenticate(username= username, password= password)
    if user is not None:
        Login(request, user)
        messages.error(request, "Please fill the form correctly")
        return redirect("/index")
    else:
        return redirect("/")

def handlesignup(request):
    a = random.randint(0,100)
    b = random.randint(0,100)
    username = request.POST['username']
    pass1 = request.POST['password1']
    pass2 = request.POST['password2']
    capt = request.POST['capt']
    ct = int(capt)
    print(ct, c)
    if ct != c:
        return redirect('/signup')
    if (pass1!= pass2):
        return redirect('/signup')

    myuser = User.objects.create_user(username, pass1, pass1)
    myuser.save()
    return redirect('/')

def add(request):
    return render(request, 'add.html')

def handleadd(request):
    title = request.POST['title']
    desc = request.POST['desc']
    img = request.FILES['uploadfrompc']
    mode = request.POST['p']
    idss = request.user.id
    p = post()
    p.title = title
    p.desc = desc
    p.thumbnail = img
    p.modes = mode
    p.ids = idss
    p.save()
    return redirect('/index')

def home(request):
    data = post.objects.all()
    a = []
    for i in data:
        if 1 == int(i.modes):
            a.append(i)
    return render(request, 'home.html', {'item': a})

def index(request):
    s = int(request.user.id)
    data = post.objects.all()
    a = []
    for i in data:
        if s == int(i.ids):
            a.append(i)
    return render(request, 'index.html', {'item': a})