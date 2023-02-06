from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate, login
from .models import User

# Create your views here.

class LoginPageView(View):
    template_name = 'authentication/authenticate.html'

    def get(self, request):
        return render(request, self.template_name)

class RegisterPageView(View):
    template_name = 'authentication/register.html'

    def get(self, request):
        return render(request, self.template_name)

def loginUser(request):
    if request.method == 'POST':    
        username = request.POST["username"]
        password = request.POST["password"]
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:  
                login(request, user)
                return render(request, 'base.html')
            try:
                user = User.objects.get(email=username)
                username = user.username
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return render(request, 'base.html')
            except User.DoesNotExist:
                return render(request, 'authentication/authenticate.html')
    return render(request, 'authentication/authenticate.html')