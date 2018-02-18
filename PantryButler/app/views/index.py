from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def inventory(request):
    return render(request, 'pb.inv.component.js')
