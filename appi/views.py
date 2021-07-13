from django.shortcuts import render
import socket
import datetime
import random
from .models import data
# Create your views here.
def index(request):
    if request.method=="GET":
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        date_time=datetime.datetime.now()
        n = random.randint(20,50)
        data=data(hostname=hostname, ip_address= ip_address,date_time=date_time,n=n)
        data.save()
    context={"hostname":hostname,"ip_address":ip_address,"date_time":date_time,"n":n}
    return render(request, 'index.html',context)

def show(request):
    if request.method=="GET":
        de=data.objects.all()
        context={"data":de}
    return render(request,'show.html',context)