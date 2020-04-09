from django.shortcuts import render

# Create your views here.
def cardsgame(request):
    return render(request,'cards/cardsgame.html')
