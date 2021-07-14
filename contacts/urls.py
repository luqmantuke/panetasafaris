from django.urls import path
from .views import contactView


urlpatterns = [
    path('contact/', contactView, name="contact"),

]
