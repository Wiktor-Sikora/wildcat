from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class LoginPageView(View):
    template_name = 'authentication/authenticate.html'

    def get(self, request):
        return render(request, self.template_name)