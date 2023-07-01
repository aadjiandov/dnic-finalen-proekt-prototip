from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class VacuumCleaner(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    picture = models.ImageField(upload_to='vacuum_cleaners/')
    description = models.TextField()

    def __str__(self):
        return self.name


class CartItem(models.Model):
    vacuumCleaner = models.ForeignKey(VacuumCleaner, on_delete=models.CASCADE)
    quantity = models.IntegerField
    subTotal = models.IntegerField

    def __init__(self, robot, quantity=1):
        self.vacuumCleaner = robot
        self.quantity = quantity


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(VacuumCleaner, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username}'s Cart"

    def total_items(self):
        return sum(item.quantity for item in self.items.all())

    def total_price(self):
        return sum(item.product.price * item.quantity for item in self.items.all())
