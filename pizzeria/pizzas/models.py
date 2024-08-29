from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)  # Optional description of the pizza
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Price of the pizza
    is_vegetarian = models.BooleanField(
        default=False
    )  # Indicates if the pizza is vegetarian
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # Timestamp when the pizza was added
    updated_at = models.DateTimeField(
        auto_now=True
    )  # Timestamp when the pizza was last updated

    def __str__(self):
        return self.name


class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, related_name="toppings", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    is_vegetarian = models.BooleanField(
        default=False
    )  # Indicates if the topping is vegetarian
    quantity = models.IntegerField(default=1)  # Quantity of the topping used

    def __str__(self):
        return self.name
