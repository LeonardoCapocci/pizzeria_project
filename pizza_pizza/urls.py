"""Defines URL patterns for pizza_pizza."""

from django.urls import path

from . import views

app_name = 'pizza_pizza'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Pizzas page
    path('pizzas/', views.pizzas, name='pizzas'),
    # A page of a single pizza's toppings
    path('pizzas/<int:pizza_id>/', views.toppings, name='pizza')
]