from django.db import models


class MealPlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name


MEAL_TIME = ["Breakfast", "Lunch", "Dinner"]


class Meal(models.Model):
    MEAL_TIMES = [
        ("breakfast", "Breakfast"),
        ("lunch", "Lunch"),
        ("dinner", "Dinner"),
    ]

    meal_plan = models.ForeignKey(
        MealPlan, on_delete=models.CASCADE, related_name="meals"
    )
    name = models.CharField(max_length=100)
    recipe = models.TextField(blank=True)
    day = models.DateField()
    meal_time = models.CharField(max_length=10, choices=MEAL_TIMES)

    def __str__(self):
        return f"{self.meal_time.capitalize()} on {self.day}: {self.name}"
