from django.shortcuts import render
from .models import Chat

# Create your views here.
def index(request):
    """
    View function for home page of site
    """
    return render(
        request,
        'index.html',
        context={},
    )
