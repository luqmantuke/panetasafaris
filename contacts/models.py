from django.db import models

class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=80)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.full_name