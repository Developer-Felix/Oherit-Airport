from ast import Subscript
from django.shortcuts import render

from core.models import Booking, Destination, Subscription

# Create your views here.
def index(request):
    destinations = Destination.objects.all().order_by('-id')
    if request.method == "POST":
        

        #Booking Post
        

        curent_location = request.POST.get('curent_location')
        to = request.POST.get('to')
        date_dep = request.POST.get('date_dep')
        time = request.POST.get('time')
        no_of_persons = request.POST.get('no_of_persons')
        type_of_aircraft = request.POST.get('type_of_aircraft')
        name   = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        # print(to)
        # print(curent_location)
        

        booking = Booking(curent_location=Destination.objects.get(id=curent_location), 
                          to = Destination.objects.get(id=to),
                          date_dep = date_dep,
                          time = time,
                          no_of_persons = no_of_persons,
                          type_of_aircraft = type_of_aircraft,
                          name = name,
                          phone = phone,
                          email = email

        )
        booking.save()
        print("done")

        #Subscription POST mail
        mail = request.POST.get('mail')
        # print(mail)
        try:
            subsciption = Subscription(mail=mail)
            subsciption.save()
            # print("done")
        except:
            # print("fail")
            pass


    data = {
        'destinations':destinations,
    }
    return render(request,'index.html',data)