from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout

from .models import User
from .forms import LoginForm

# Create your views here.

class LoginPageView(View):
    template_name = 'authentication/authenticate.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'login_form': LoginForm()})
    
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                if not form.cleaned_data['remember_me']:
                    request.session.set_expiry(0)
                return redirect('products:index')                
        return render(request, self.template_name, {'login_form': form})

class RegisterPageView(View):
    template_name = 'authentication/register.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)

class LogOutPageView(View):
    def get(self, request):
        logout(request)
        return redirect('products:index', permanent=True)