from django.db import models
from phone_field import PhoneField
from django.shortcuts import render, redirect
from django.urls import reverse


category_tuple = (("deluxe room","deluxe room"),("super deluxe room","super deluxe room"),("suite room","suite room"))
state_tuple = (("Occupied","Occupied"),("Booked","Booked"),("Available","Available"))


class RoomInfo(models.Model):
	category = models.CharField(max_length=50, choices = category_tuple, default = "deluxe room")
	state = models.CharField(max_length=50, choices=state_tuple, default="Available")
	room_contact = PhoneField(blank = True)
	remark = models.TextField(default="")

	def __str__(self):
		return self.remark

class BookRoom(models.Model):
	customer_name = models.CharField(max_length = 50)
	customer_contact = PhoneField(blank=True)
	room_category = models.CharField(max_length=50, choices = category_tuple, default = "deluxe room")
	room_no = models.CharField(max_length=10)
	
	checkin_date = models.DateField( blank = True , null = True)
	checkout_date = models.DateField( blank = True , null = True )
	days = models.IntegerField(default=0)
	remark = models.TextField()
	room = models.ForeignKey(RoomInfo, on_delete = models.CASCADE, null = True, blank = True)
	has_checkedin = models.BooleanField(default= False)
	has_checkedout = models.BooleanField(default = False)

	def __str__(self):
		return self.customer_name

	def get_absolute_url(self):
		return reverse('home')	
	


class CheckIn(models.Model):
	room_no = models.IntegerField(default=0)
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('home')

class CheckOut(models.Model):
	room_no = models.IntegerField(default=0)
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('home')

