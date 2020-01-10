from django.shortcuts import render
from django.views import View


class LandingPageView(View):
    def get(self, request):
        return render(request, 'index.html', {})

    def post(self, request):
        pass


class DonationView(View):
    def get(self, request):
        return render(request, 'form.html', {})
    pass


class LoginView(View):
    pass


class RegisterView(View):
    pass
