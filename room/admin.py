from django.contrib import admin
from .models import BookRoom, RoomInfo, CheckIn, CheckOut

admin.site.register(BookRoom)
admin.site.register(RoomInfo)
admin.site.register(CheckIn)
admin.site.register(CheckOut)