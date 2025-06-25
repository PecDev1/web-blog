from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm, CustomLoginForm
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def login_register_view(request):
    login_form = AuthenticationForm()
    signup_form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'login_form': login_form,
        'signup_form': signup_form
    })

from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    authentication_form = CustomLoginForm
    template_name = 'registration/login.html'


from django.shortcuts import render
from .forms import RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Formani qayta ishlang (saqlang, email yuboring va h.k.)
            pass
    else:
        form = RegistrationForm()

    return render(request, 'your_template.html', {'form': form})
