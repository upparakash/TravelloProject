from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth,User
from .models import *
from django.core.paginator import Paginator
# Create your views here.
def register(request):
     if request.method=="POST":
          firstname = request.POST['firstname']
          lastname = request.POST['lastname']
          email = request.POST['email']
          username = request.POST['username']
          password1 = request.POST['password1']
          password2 = request.POST['password2']
          if password1 == password2:
              if User.objects.filter(username=username).exists():
                  messages.info(request,"username already exist")
                  return redirect("register")
              elif User.objects.filter(email=email).exists():
                  messages.info(request," email already exist ")
                  return redirect("register")
              else:
                  user=User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password1)
                  user.save()
                  print("user created")
                  return redirect('fun')
          else:
             messages.info(request,"password not matched")
             return redirect('register')

     else:
      # messages.info(request,"password error")
      return render(request, 'registration.html')

def login(request):
    if request.method=='POST':
        username= request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid user")
            return redirect("Login")
    else:
      return render(request,"Login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')


def news(request):
    data=News.objects.all().order_by('-create_date')
    paginator= Paginator(data,3)
    page = request.GET.get('page')
    print(page)
    paged_news = paginator.get_page(page)
    print("paged_news",paged_news)
    return render(request,'News.html',{'news':paged_news})



def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['Name']
        email = request.POST['Email']
        subject = request.POST['Subject']
        message = request.POST['Message']
        store = info.objects.create(name=name,email=email,subject=subject,message=message)
        admin_detail=User.objects.get(is_superuser=True)
        admin_email=admin_detail.email
        send_mail(
            'You have a new travel inquiry',
            ' Check out new inquiry with Name: ' + name + ' and email: '+ email + ' Please login to admin pannel for more detail' ,
            'myweddingcorp23@gmail.com', #from email address
            [admin_email], #To email address
            fail_silently=False,
                 )

        store.save()
    return render(request,'contacts.html')

def footer(request):
    if request.method == 'POST':
      name = request.POST['name']
      email = request.POST['email']
      admin_detail=User.objects.get(is_superuser=True)
      admin_email=admin_detail.email
      send_mail(
        'You have a new subscribtion',
        'Have a new subscription !! with Name: ' + name + ' and email: '+ email + ' Please login to admin pannel for more detail' ,
        'myweddingcorp23@gmail.com', #from email address
        [admin_email], #To email address
        fail_silently=False,
             )
    return redirect('/')
# def search(request):
#     if request.method == "POST":
#         city = request.POST['city']
#         departure = request.POST['departure']
#         arrival = request.POST['arrival']
#         budget = request.POST['budget']
#         use = User.objects.create_user(city_search=city,departure_search=departure,arrival_search=arrival,budget_search=budget)
#         use.save()
#         return redirect('/')
#     else:
#         return render(request, '/')

def logout(request):
    if request.method == 'POST':
     auth.logout(request)
    return redirect('login')
