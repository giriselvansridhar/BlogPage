from django.shortcuts import render,redirect
from .models import Room
from .forms import RoomForm



# Create your views here.






def home(request):
    rooms=Room.objects.all()
    return render(request,'base/home.html',{'rooms':rooms})


def room(request,pk):

    

    room=Room.objects.get(id=int(pk))

    context={'room':room}        
    return render(request,'base/room.html',context)



def create_room(request):
    form=RoomForm()


    if request.method=='POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form':form}
    return render(request,'base/room_form.html', context)



def UpdateRoom(request,pk):
    room=Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method =='POST':
            form =RoomForm(request.POST, instance=room)
            if form.is_valid():
                 form.save()
                 return redirect('home')
            

    

    context={'form':form}
    return render(request,'base/room_form.html',context)







def deleteRoom(request,pk):
     room=Room.objects.get(id=pk)
     if request.method=='POST':
          room.delete()
          return redirect('home')
     
     return render(request,'base/room_delete.html',{'obj':room})