from django.shortcuts import render
from .models import Destination

# Create your views here.


def index(request):

    dest1 = Destination()
    return render(request, "index.html", {"dest1": dest1})
