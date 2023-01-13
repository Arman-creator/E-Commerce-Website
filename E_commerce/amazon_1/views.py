from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "../templates/index.html")

def orders(request):
    return HttpResponse("This is orders page")#Here on going to /ordres we get this plain text but later we will render htlm files from here

def cart(request):
    return HttpResponse("This is cart page")

