from django.urls import path
from . import views

urlpatterns=[
	path('',views.index, name="index"),
	path('basic',views.basic, name="basic"),
	path('rooms',views.rooms, name="rooms")
]