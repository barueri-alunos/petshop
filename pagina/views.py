from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'index.html')


def pessoas(request):
    
    return render(request, 'pessoas.html')


def cadastrar_pet(request):

    return render(request, 'cadastro-pet.html')

def login(request):

    return render(request, 'login.html')