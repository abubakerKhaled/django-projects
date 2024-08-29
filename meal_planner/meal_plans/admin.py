from django.contrib import admin
from .models import MealPlan, Meal


class MealAdmin(admin.ModelAdmin):
    list_display = ["name", "meal_plan", "day", "meal_time"]
    search_fields = ["meal_time"]


# Registering models with the admin site
admin.site.register(MealPlan)
admin.site.register(Meal, MealAdmin)
