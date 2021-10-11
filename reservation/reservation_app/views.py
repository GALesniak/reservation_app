from django.shortcuts import render, redirect
from .forms import RoomForm, BookingForm
from .models import Room, Booking
from reservation_app.booking_logic.availability import is_available


# Create your views here.

def admin_view(request):
    """view where you can add, remove, modify rooms"""
    context = {'room_list': Room.objects.all()}
    return render(request, "reservation_app/admin.html", context)


def welcome_view(request):
    """main page"""
    return render(request, "reservation_app/index.html")


def room_list(request):
    """list of all available rooms"""
    context = {'room_list': Room.objects.all()}
    return render(request, "reservation_app/room_list.html", context)

def room_details(request, id):
    """booking of a specific room"""
    specific_room = Room.objects.get(pk=id)
    form = BookingForm()
    if request.method == 'GET':
        return render(request, 'reservation_app/room_details.html',
                      {'specific_room': specific_room, 'form' : form})
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if is_available(specific_room, data['check_in'], data['check_out']):
                booking = Booking.objects.create(
                    room_id=id,
                    room=specific_room,
                    booking_in=data['check_in'],
                    booking_out=data['check_out']
                )
                booking.save()
            else:
                return redirect("fail_view")
        return redirect('success_view')
    context = {'form': form, 'specific_room': specific_room}
    return render(request, f'reservation_app/room_details.html, {context}')


def room_form(request, id=0):
    """functionalities : add, modify room"""
    if request.method == "GET":
        if id == 0:
            form = RoomForm()
        else:
            room = Room.objects.get(pk=id)
            form = RoomForm(instance=room)
        return render(request, "reservation_app/room_form.html", {'form': form})
    else:
        if id == 0:
            form = RoomForm(request.POST)
        else:
            room = Room.objects.get(pk=id)
            form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
        return redirect('/user_admin')


def room_delete(request, id):
    """function: delete room"""
    room = Room.objects.get(pk=id)
    room.delete()
    return redirect('/room/list')


def success_view(request):
    """view shown when reservation was successful - room is free to book"""
    return render(request, 'reservation_app/success.html')

def fail_view(request):
    """view shown when reservation was unsuccessful - room is occupied at this time"""
    return render(request, 'reservation_app/fail.html')