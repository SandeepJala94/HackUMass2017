from django.shortcuts import render
from .models import Chat


# Create your views here.
def index(request):
    """
    View function for home page of site
    """
    chat_item = request.POST.get('content')
    chat = Chat.objects.all()
    return render(
        request,
        'index.html',
        context={
            'chat': chat,
        },
    )
