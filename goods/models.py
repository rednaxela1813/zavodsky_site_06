import uuid

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

"""
Create product management models.
There must be categories, products, and their properties.
Unlimited number of properties (separate property table with many-to-many relationships)
"""


class Address(models.Model):
    #uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
    #uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    CHOICE = (('home', 'Home'), ('work', 'Work'), ('mobile', 'Mobile'))
   
    #name = models.CharField(max_length=255)
    number = PhoneNumberField(blank=True)
    type = models.CharField(max_length=255, choices=CHOICE, default='mobile')

    def __str__(self):
        return f'{self.number} ({self.type})'

    class Meta:
        verbose_name_plural = 'Phones'
        ordering = ['number']


class Photo(models.Model):
   # uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='static/deps/images/prenajom/photos/', blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.IntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name_plural = 'Photos'
        ordering = ['image']

    def __str__(self):
        return self.image.url if self.image else 'No Image'


class Category(models.Model):
   # uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def get_photos(self):
        content_type = ContentType.objects.get_for_model(self)
        return Photo.objects.filter(content_type=content_type, object_id=self.id)

    def __str__(self):
        return self.name


class Product(models.Model):
   # uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, related_name='products')
   # property = models.ManyToManyField('Property', blank=True, related_name='products')
    address = models.OneToOneField(Address, on_delete=models.CASCADE, blank=True, related_name='product')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photos_product = models.ManyToManyField(Photo, blank=True, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    phone_number = models.ForeignKey(Phone, on_delete=models.CASCADE, blank=True, related_name='products')
    email = models.ForeignKey('Email', on_delete=models.CASCADE, blank=True, related_name='products')

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
  #  uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True)
    object_id = models.IntegerField(blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    

    


class Email(models.Model):
  #  uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=False)
    
    def __str__(self):
        return self.email

    class Meta:
        ordering = ['email']
