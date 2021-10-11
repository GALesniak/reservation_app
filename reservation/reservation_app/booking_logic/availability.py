
from reservation_app.models import Booking



def is_available(room, check_in, check_out):
    """check whether room might be booked or is occupied already"""
    availability_list = []
    booking_list = Booking.objects.filter(room=room)
    for booking in booking_list:
        if booking.booking_in > check_out or booking.booking_out < check_in:
            availability_list.append(True)
        else:
            availability_list.append(False)
    return all(availability_list)


