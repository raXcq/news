from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm


# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy(
        "login"
    )  # Redirect to the login page after successful signup
    template_name = "registration/signup.html"  # Path to your signup template
