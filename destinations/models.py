from django.db import models
from django.db.models.signals import pre_save
from ckeditor.fields import RichTextField
from django.urls import reverse
from panetasafaris.utils import unique_slug_generator

tour_list = [
    ('Trekking', "Trekking"),
    ('Safari', "Safari"),
    ('Island', "Island"),
    ('More', "More")
]


class Destination(models.Model):
    image = models.ImageField(upload_to='media')
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    destination_type = models.CharField(choices=tour_list, max_length=20)
    slug = models.SlugField(max_length=250, blank=True, null=True)
    tour_descr = RichTextField(blank=True, null=True)
    duration = models.CharField(max_length=100, null=True)
    popular = models.BooleanField(max_length=10, blank=True, null=True)
    price = models.PositiveIntegerField(null=True)

    def get_absolute_url(self):
        return reverse("destinationdetails", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name

class Bookings(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=255, null=True)
    tour_name = models.CharField(max_length=255, null=True)
    quantity = models.PositiveIntegerField()
    message = models.TextField(blank=True, null=True)
    tour = models.ForeignKey(Destination, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.full_name




def slug_generator(sender, instance, *args, **kwargs): 
    if not instance.slug: 
        instance.slug = unique_slug_generator(instance) 


pre_save.connect(slug_generator, sender = Destination)