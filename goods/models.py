from os import name
import uuid

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

"""
create product management models.
There must be categories, products and its properties.
 Unlimited number of properties (separate property table with many-to-many relationships)
"""


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.street}, {self.city}, {self.state}, {self.country}, {self.postal_code}'

    class Meta:
        verbose_name_plural = 'Addresses'
        ordering = ['street']


class Phone(models.Model):
    CHOICE = (('home', 'Home'), ('work', 'Work'), ('mobile', 'Mobile'))
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    number = PhoneNumberField(blank=True, null=True)
    type = models.CharField(max_length=255, choices=CHOICE, default='mobile')

    def __str__(self):
        return f'{self.number} ({self.type})'

    class Meta:
        verbose_name_plural = 'Phones'
        ordering = ['number']


class Photo(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='static/deps/images/prenajom/photos/', blank=True, null=True)
    #product_photo = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='photos')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name_plural = 'Photos'
        ordering = ['image']

    def __str__(self):
        return self.image.url


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def get_photos(self):
        content_type = ContentType.objects.get_for_model(self)
        return Photo.objects.filter(content_type=content_type, object_id=self.id)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    #photos_product = models.OneToOneField(Photo, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    phone_number = models.ForeignKey(Phone, on_delete=models.CASCADE, blank=True, null=True)
    email  = models.ForeignKey('Email', on_delete=models.CASCADE, blank=True, null=True)


    def get_photos(self):
        content_type = ContentType.objects.get_for_model(self)
        return Photo.objects.filter(content_type=content_type, object_id=self.id)
    
    
    def get_properties(self):
        content_type = ContentType.objects.get_for_model(self)
        return Property.objects.filter(content_type=content_type, object_id=self.id)


    def __str__(self):
        return self.name
    

    class Meta:
        ordering = ['name']


class Property(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    products = models.ManyToManyField(Product, related_name='properties')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']



class Email(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True)
    
    def __str__(self):
        return self.email

    class Meta:
        ordering = ['email']

