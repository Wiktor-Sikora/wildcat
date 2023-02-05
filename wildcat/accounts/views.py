from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class LoginPageView(View):
    template_name = 'authentication/authenticate.html'

    def get(self, request):
        return render(request, self.template_name)

class RegisterPageView(View):
    template_name = 'authentication/register.html'

    def get(self, request):
        return render(request, self.template_name)