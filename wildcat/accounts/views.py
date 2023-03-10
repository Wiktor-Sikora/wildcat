from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.views.generic.edit import DeleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.db.models import Max, Count

from products.models import Product, Image
from accounts.forms import LoginForm, RegisterForm, UpdateProfileForm

# Create your views here.

User = get_user_model()

class LoginPage(View):
    template_name = 'authentication/authenticate.html'

    def get(self, request):
        logout(request)
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
            form.add_error(None, 'Sorry, that login was invalid. Please try again.')
        return render(request, self.template_name, {'login_form': form})

class RegisterPage(View):
    template_name = 'authentication/register.html'

    def get(self, request):
        logout(request)
        return render(request, self.template_name, {'register_form': RegisterForm()})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('products:index', permanent=True)
        return render(request, self.template_name, {'register_form': form})

class LogOutPage(View):
    def get(self, request):
        logout(request)
        return redirect('products:index', permanent=True)
    
class AccountPage(View):
    template_name = 'users/profile.html'

    def get(self, request, slug):
        account = get_object_or_404(User, slug=slug)
        account_following = User.follows.through.objects.filter(from_user=account).count()
        products = Product.objects.filter(owner=account)[50:].annotate(Count('stars'))
        favorite = Product.objects.filter(stars=account)[50:].annotate(Count('stars'))
        return render(request, self.template_name, {'account': account, 'account_following': account_following, 'products': products, 'favorite': favorite})

class AccountSettingsPage(View):
    def get(self, request):
        return render(request, 'users/settings.html', {'form': UpdateProfileForm(instance=request.user)})

    def post(self, request):
        form = UpdateProfileForm(request.POST or None, request.FILES or None, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account updated successfully')
            return redirect('accounts:settings', permanent=True)
        messages.error(request, 'Something went wrong while updating an account')
        return render(request, 'users/settings.html', {'form': form})

class AccountDelete(DeleteView):
    model = User
    success_url = ''
    
