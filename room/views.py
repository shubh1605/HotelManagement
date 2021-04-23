from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import BookRoom, RoomInfo, CheckIn, CheckOut
from django.contrib import messages 
from django.urls import reverse
import datetime


def checkAvailability(room_cat, checkin, checkout):

	Rooms = BookRoom.objects.filter(checkin_date__lte =  checkin , checkout_date__gte = checkin, room_category = room_cat) | BookRoom.objects.filter(checkin_date__lte =  checkout , checkout_date__gte = checkout,  room_category = room_cat) | BookRoom.objects.filter(checkin_date__gte =  checkin , checkout_date__lte = checkout, room_category = room_cat)
	print(Rooms)
	for i in Rooms:
		print("i: ",i.room.id)
		RoomInfo.objects.filter(id = i.room.id).update(state="Booked")
		print("a: ",RoomInfo.objects.filter(id = i.room.id))	
	
	available = RoomInfo.objects.filter(category=room_cat, state= "Available")

	
	if(len(available) != 0):
		room_no = available[0].id 
	

	for i in Rooms:
		print("i: ",i.room.id)
		RoomInfo.objects.filter(id = i.room.id).update(state="Available")
		print("a: ",RoomInfo.objects.filter(id = i.room.id))
	
	
	if(len(available) == 0):
		return -1
	else:
		return room_no


def home(request):
	if request.method == "POST":
		customer_name = request.POST['customer_name']
		room = BookRoom.objects.filter(customer_name__contains = customer_name) | BookRoom.objects.filter(customer_contact__contains = customer_name)
		context={
		"rooms": room
		}
		return render(request, "room/home.html", context)

	else:
		room = BookRoom.objects.all()
		context={
		"rooms": room
		}
		return render(request, "room/home.html", context)

def cancel_booking(request, pk):
	if request.method == "POST":		
		print(pk)
		BookRoom.objects.filter(id = pk).delete()
		messages.error(request, "Booking Cancelled")
	return redirect('home')	

class AddRoomView(CreateView):
	model = BookRoom
	fields = ['customer_name','customer_contact',
				'room_category', 'checkin_date',
				'checkout_date', 'days', 'remark']

	def form_valid(self, form):
		category = form.instance.room_category	
		checkin = form.instance.checkin_date
		checkout = form.instance.checkout_date

		avail = checkAvailability(category, checkin, checkout)
		if(avail == -1):
			messages.error(self.request,  'Not enough rooms available!')
			return super().form_invalid(form)
		else:
			messages.success(self.request,  'You have been alloted room '+str(avail))
			room_alloted = RoomInfo.objects.filter(id = avail)[0]
			print("room: ", room_alloted)
			
			
			form.instance.room = room_alloted
			print(form.instance.room )
			form.instance.room_no = avail
		print(avail)
		return super().form_valid(form)

class CheckInView(CreateView):
	model = CheckIn
	fields = ['room_no','name']

	def form_valid(self, form):
		alloted = BookRoom.objects.filter(room_no= form.instance.room_no, customer_name = form.instance.name, checkin_date = datetime.date.today())
		
		if(len(alloted)==0):
			messages.error(self.request,'No rooms booked !')
			return super().form_invalid(form)
		else:
			if(alloted[0].has_checkedin):
				messages.error(self.request,'Already has checked in once !')
				return super().form_invalid(form)
			else:	
				messages.success(self.request,  "Welcome to the hotel")
				alloted.update(has_checkedin =True )
			

		return super().form_valid(form)

class CheckOutView(CreateView):
	model = CheckOut
	fields = ['room_no','name']

	def form_valid(self, form):
		alloted = BookRoom.objects.filter(room_no= form.instance.room_no, customer_name = form.instance.name, checkout_date = datetime.date.today())
		
		if(len(alloted)==0):
			messages.error(self.request,  'Wrong room chosen !')
			return super().form_invalid(form)
		else:
			if(alloted[0].has_checkedin):
				if(alloted[0].has_checkedout):

					messages.error(self.request, "You have already checked out! ")
					return super().form_invalid(form)
				else:
					if(alloted[0].room_category == "deluxe room"):
						bill = alloted[0].days * 2500
					elif(alloted[0].room_category == "super deluxe room"):
						bill = alloted[0].days * 5000
					else:
						bill = alloted[0].days * 8000

					messages.success(self.request,  "Please pay Rs "+str(bill) +"/-. Thank you for choosing our hotel. Visit again :) " )
					alloted.update(has_checkedout =True )
			else:
				messages.error(self.request, "You never checked in")
				return super().form_invalid(form)
			

		return super().form_valid(form)


def available(request):
	fields = ['checkin','checkout', 'category']
	if request.method == "POST":
		# print(datetime.date.today())
		room_cat = request.POST['category']
		checkin = request.POST['checkin']
		checkout = request.POST['checkout']

		print(checkin)
		print(checkout)
		print(room_cat)

		Rooms = BookRoom.objects.filter(checkin_date__lte =  checkin , checkout_date__gte = checkin, room_category = room_cat) | BookRoom.objects.filter(checkin_date__lte =  checkout , checkout_date__gte = checkout,  room_category = room_cat) | BookRoom.objects.filter(checkin_date__gte =  checkin , checkout_date__lte = checkout, room_category = room_cat)
		print(Rooms)
		for i in Rooms:
			print("i: ",i.room.id)
			RoomInfo.objects.filter(id = i.room.id).update(state="Booked")
			print("a: ",RoomInfo.objects.filter(id = i.room.id))	
		
		available = RoomInfo.objects.filter(category=room_cat, state= "Available")
		print(len(available))
		context={
		"rooms_available" : len(available)
		}

		for i in Rooms:
			print("i: ",i.room.id)
			RoomInfo.objects.filter(id = i.room.id).update(state="Available")
			print("a: ",RoomInfo.objects.filter(id = i.room.id))
		
		return render(request, "room/availability.html", context)
	else:
		context={
		"rooms_available" : 0,
		"checkin": datetime.date.today(),
		"checkout": datetime.date.today()
		}
		return render(request, "room/availability.html", context)
