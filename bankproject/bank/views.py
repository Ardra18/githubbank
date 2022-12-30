from django.shortcuts import render


def index(request):
    return render(request,"index.html")
def trv(request):
    return render(request,"trv.html")
def kol(request):
    return render(request,"kol.html")
def alapuzha(request):
    return render(request,"alapuzha.html")
def ekm(request):
    return render(request,"Ekm.html")
def kannur(request):
    return render(request,"kannur.html")


