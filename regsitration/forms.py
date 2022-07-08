from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm

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
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',
                  )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.atters['class'] = 'form-control'
        self.fields['password1'].widget.atters['class'] = 'form-control'
        self.fields['password2'].widget.atters['class'] = 'form-control'


class EditProfileForm(UserChangeForm):
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))

    username = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    last_login = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    is_superuser = forms.CharField(
        max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))

    is_staff = forms.CharField(
        max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))

    is_active = forms.CharField(
        max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))

    date__joined = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))


class Meta:
    model = User
    fields = ('first_name', 'last_name', 'email', 'username', 'last_login',
              'is_superuser', 'is_staff', 'is_active', 'date__joined')


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
