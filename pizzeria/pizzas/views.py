from django.shortcuts import render, get_object_or_404
from .models import Pizza, Topping
def index(request):
    return render(request, 'pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.all()
    return render(request, 'pizzas/pizzas.html', {'pizzas': pizzas})

def topping(request, pizza_id):
    pizza = get_object_or_404(Pizza, pk=pizza_id)
    toppings = pizza.toppings.all()
    return render(
        request, "pizzas/topping.html", {"pizza": pizza, "toppings": toppings}
    )
