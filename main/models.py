from turtle import title
from django.db import models
from goods.models import Address, Phone, Email


class Contact(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null=True)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE, blank=True, null=True)
    ico = models.CharField(max_length=255, blank=True, null=True)
    dic = models.CharField(max_length=255, blank=True, null=True)
    ic_dph = models.CharField(max_length=255, blank=True, null=True)
    email = models.ForeignKey(Email, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.title
    


