import uuid
from django.db import models



class Menu(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    home = models.CharField(max_length=50, blank=True, null=True)
    about = models.CharField(max_length=50, blank=True, null=True)
    services = models.CharField(max_length=50, blank=True, null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)
    login = models.CharField(max_length=50, blank=True, null=True)
    logout = models.CharField(max_length=50, blank=True, null=True)
    register = models.CharField(max_length=50, blank=True, null=True)
    profile = models.CharField(max_length=50, blank=True, null=True)
    dashboard = models.CharField(max_length=50, blank=True, null=True)
    admin = models.CharField(max_length=50, blank=True, null=True)
    users = models.CharField(max_length=50, blank=True, null=True)
    groups = models.CharField(max_length=50, blank=True, null=True)
    permissions = models.CharField(max_length=50, blank=True, null=True)
    settings = models.CharField(max_length=50, blank=True, null=True)
    help = models.CharField(max_length=50, blank=True, null=True)
    search = models.CharField(max_length=50, blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)
    theme = models.CharField(max_length=50, blank=True, null=True)
    light = models.CharField(max_length=50, blank=True, null=True)
    dark = models.CharField(max_length=50, blank=True, null=True)
    

    def __str__(self):
        return f"{self.uuid}"
