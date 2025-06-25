from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.views import View
from django.urls import reverse

class HomePageView(TemplateView):
    template_name = 'home.html'

class LogoutPageView(View):
    def get(self, request, *args, **kwargs):
        logout(request)  # Log the user out
        next_page = request.GET.get('next', reverse('home'))  # Default to 'home' if not provided
        return redirect(next_page)  # Redirect to the specified page

def CallCenterPageView(request):
    # Assuming this should handle user sign-up or login.
    # Replace 'home.html' with the appropriate template for signing in or signing up.
    return render(request, 'registration/call_center.html')  # Change as needed

def AboutPaggeView(request):
    return render(request, 'about.html')
def GamesPageView(request):
    return render(request, 'games/main_games_page.html')
