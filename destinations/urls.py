from django.urls import path
from .views import destination_list, destination_details

urlpatterns = [
    path('destinations/', destination_list, name="destinationlist"),
    path('destinations/<slug:slug>/', destination_details, name="destinationdetails"),
]
