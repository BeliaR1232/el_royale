from django.urls import path

from .api.views import (RoomInfoView, RoomCreateView, RoomDeleteView,
                        BookingInfoView, BookingCreateView, BookingDeleteView)


urlpatterns = [
    path('rooms/', RoomInfoView.as_view()),
    path('bookings/', BookingInfoView.as_view()),
    path('rooms/create/', RoomCreateView.as_view()),
    path('bookings/create/', BookingCreateView.as_view()),
    path('rooms/delete/<int:pk>', RoomDeleteView.as_view()),
    path('bookings/delete/<int:pk>', BookingDeleteView.as_view()),
]
