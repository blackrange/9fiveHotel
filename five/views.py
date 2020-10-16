from django.shortcuts import render
from .models import RoomType

# Create your views here.
def index(request):
    return render(request,'index.html')

def basic(request):
    return render(request,'basic.html')

def rooms(request):
    roomData=RoomType()
    roomData.roomName="Single Room"
    roomData.price=100
    roomData.details="best valued room"


    return render(request,'rooms.html', {'roomData' : roomData})