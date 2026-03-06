from django.db import models
from apps.core.models import Product

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    adress = models.TextField()
    message = models.TextField(blank=True)

    class Status(models.TextChoices):
        PENDING = "Pending", "pending"
        CONFIREMENT = "Confirment", "confirment"
        CANCLED = "Cancled", "cancled"

    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.product}'
    
class Feedback(models.Model):
    name = models.CharField(max_length=50)
    role = models.TextField(blank=True)
    message = models.TextField()
    rating = models.PositiveSmallIntegerField()
    is_aprove = models.BooleanField(default=False)
    submited_at = models.DateTimeField(auto_now_add=True)