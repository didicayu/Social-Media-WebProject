from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")  # Redirect to the login page after a successful registration
    template_name = "registration/signup.html"  # The template used to render the page
