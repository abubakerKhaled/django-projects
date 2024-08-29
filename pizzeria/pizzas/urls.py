from django.urls import path
from . import views

app_name = "pizzas"

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Pizzas details page
    path('pizzas/', views.pizzas, name='pizzas'),
    
    # Topping for each Pizza
    path('topping/<int:pizza_id>', views.topping, name='topping'),
]
