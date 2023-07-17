from django.db import models
from authentication.models import CustomUser

# Create your models here.


class Product(models.Model):
    user = models.ForeignKey(CustomUser, default=1, on_delete=models.CASCADE)
    name = models.CharField(blank=False, null=False, max_length=255)
    specification = models.CharField(blank=True, null=True, max_length=255)
    color = models.CharField(blank=True, null=True, max_length=255)
    availability = models.BooleanField(default=False, blank=False, null=False)
    quantity = models.IntegerField(blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return str(self.id)+self.name
