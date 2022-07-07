from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import SignUpForm, EditProfileForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Sign Up View


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


class UserEditView(UpdateView):
    form_class = EditProfileForm

    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
