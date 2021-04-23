from django.urls import path
from .views import AddRoomView, CheckInView, CheckOutView
from . import views

urlpatterns =[
	path('room/book', AddRoomView.as_view(), name='add-room'),
	path('room/checkin', CheckInView.as_view(), name='check-in'),
	path('room/checkout', CheckOutView.as_view(), name='check-out'),
	path('room/available', views.available, name='availability'),
	path('room/cancel/<int:pk>',views.cancel_booking, name='cancel-booking'),
	path('',views.home, name='home'),
	
]