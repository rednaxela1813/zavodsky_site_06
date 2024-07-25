from operator import iconcat
from os import name
import uuid
from django.db import models
from goods.models import Address, Phone, Email


class ContactFormModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.ForeignKey(Email, on_delete=models.CASCADE, unique=False)
    ico = models.CharField(max_length=100)
    dic = models.CharField(max_length=100)
    link_google_maps = models.TextField(blank=True, null=True)
    ic_dph = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    