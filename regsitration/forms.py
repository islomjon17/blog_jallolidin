from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Sign Up Form


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(
        max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(
        max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]

    # def __init__(self, *args, **kwargs):
    #     super(SignUpForm, self).__init__(*args, **kwargs)

    #     self.fields['username'].widget.atters['class'] = 'form-control'
    #     self.fields['password1'].widget.atters['class'] = 'form-control'
    #     self.fields['password2'].widget.atters['class'] = 'form-control'


class EditProfileForm(UserChangeForm):
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(
        max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(
        max_length=254, help_text='Enter a valid email address')
    username = forms.CharField(
        max_length=30, required=False, help_text='Optional')
    last_login = forms.CharField(
        max_length=30, required=False, help_text='Optional')
    is_superuser = forms.CharField(
        max_length=30, required=False, help_text='Optional')
    is_staff = forms.CharField(
        max_length=30, required=False, help_text='Optional')
    is_active = forms.CharField(
        max_length=30, required=False, help_text='Optional')
    date__joined = forms.CharField(
        max_length=30, required=False, help_text='Optional')


class Meta:
    model = User
    fields = [
        'first_name',
        'last_name',
        'email',
        'username',
        'last_login',
        'is_superuser',
        'is_staff',
        'is_active',
        'date__joined',
    ]
