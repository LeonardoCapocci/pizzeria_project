from django.shortcuts import render

# Create your views here.
def index(request):
    """The home page for Pizza Recipe List."""
    return render(request, 'pizza_pizza/index.html')
