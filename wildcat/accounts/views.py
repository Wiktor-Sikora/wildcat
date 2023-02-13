from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib import messages

from .forms import LoginForm, RegisterForm

# Create your views here.

User = get_user_model()

class LoginPage(View):
    template_name = 'authentication/authenticate.html'

    def get(self, request):
        return render(request, self.template_name, {'login_form': LoginForm()})
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                if not form.cleaned_data['remember_me']:
                    request.session.set_expiry(0)
                return redirect('products:index', permanent=True)
        return render(request, self.template_name, {'login_form': form})

class RegisterPage(View):
    template_name = 'authentication/register.html'

    def get(self, request):
        return render(request, self.template_name, {'register_form': RegisterForm()})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('products:index', permanent=True)
        print(form.errors)
        return render(request, self.template_name, {'register_form': form})

class LogOutPage(View):
    def get(self, request):
        logout(request)
        return redirect('products:index', permanent=True)
    
class UserPage(View):
    def get(self, request, slug):
        user = User.objects.filter(slug=slug)
        pass
