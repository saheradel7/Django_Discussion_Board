from django.shortcuts import render
from .models import Board
# Create your views here.
def BoardList(request):
    boards = Board.objects.all()
    return render(request , 'home.html', {'boards':boards})