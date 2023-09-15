from django.shortcuts import render
from .models import Pizza

# Create your views here.
def index(request):
    """The home page for Pizza Recipe List."""
    return render(request, 'pizza_pizza/index.html')

def pizzas(request):
    """The page that lists all tracked pizzas."""
    pizzas = Pizza.objects.order_by('date_added')
    context = {'pizzas':pizzas}
    return render(request, 'pizza_pizza/pizzas.html', context)

def toppings(request, pizza_id):
    """The page that lists a single pizza's toppings."""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.toppings_set.order_by('-date_added')
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizza_pizza/pizza.html', context)
