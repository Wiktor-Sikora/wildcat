from django.shortcuts import render

# Create your views here.

def mega_test(request):
    return render(request, 'base.html')