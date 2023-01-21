from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from . models import *
from accounts .models import *
from django.db.models import Q
def home(request):
    obj=place.objects.all().order_by("-created_date")
    pack=Packages.objects.all().order_by('-create_date')
    test=Testimonials.objects.all()
    return render(request, 'index.html',{'results':obj,'package':pack,'test':test})


# def destination(request):
#     Destination=place.objects.all().order_by("-created_date")
#     return render(request,'destination.html',{'destination':Destination})

def search(request):
    if 'Place' in request.GET:
        Place = request.GET['Place']
        if Place:
            location=place.objects.all().filter(name__iexact=Place)

    if 'Arrival' in request.GET:
        arrival=request.GET['Arrival']
        if arrival:
            location=place.objects.all().filter(Arrival__iexact=arrival)

    if 'Departure' in request.GET:
        departure = request.GET['Departure']
        if departure:
            location = place.objects.all().filter(Departure__iexact=departure)

    if 'budget' in request.GET:
        budget= request.GET['budget']
        price=place.objects.values('price')
        print(price)
        if budget :
            location = place.objects.all().filter(price__lte=budget)

    if 'Place' in request.GET:
        Place = request.GET['Place']
        if 'Arrival' in request.GET:
            arrival = request.GET['Arrival']
            if 'Departure' in request.GET:
                departure = request.GET['Departure']
                if 'budget' in request.GET:
                    budget = request.GET['budget']
                    location = place.objects.all().filter(Q(name__icontains=Place) & Q(Arrival__icontains=arrival) & Q(
                        Departure__icontains=departure) & Q(price__icontains=budget))

    # if 'Arrival' in request.GET:
        #     arrival = request.GET['Arrival']
        #     if 'Departure' in request.GET:
        #         departure = request.GET['Departure']
        #         if 'budget' in request.GET:
        #             Budget = request.GET['budget']
        #             location = place.objects.all().filter(Q(name__icontains=Place)|Q(Arrival__icontains=arrival)|Q(Departure__icontains=departure)|Q(price__icontains=Budget))
    print(location)
    return render(request, 'destination.html', {'destination': location})
@login_required(login_url='login')
def fullview(request,id):
    data=place.objects.all().filter(id=id)
    return render(request,"detail.html",{"destination":data})

    #     return render(request, 'destination.html', {'destination': location})
    # if 'Arrival'in request.GET:
    #     arrival=request.GET['Arrival']
    #     taking=place.objects.all().filter(Q(model__iexact=arrival)|Q)
def About(request):
    Team=team.objects.all().order_by("-created_date")
    return render(request,"about.html",{'team':Team})