# server/forms.py
from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100, required=True, widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
    password = forms.CharField(label='Password', max_length=100, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))


class CreateUserForm(forms.Form):
    first_name = forms.CharField(
        label='First Name', 
        max_length=100, 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your first name'}))
    
    last_name = forms.CharField(
        label='Last Name',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your last name'}))
    
    email = forms.EmailField(
        label='Email',
        max_length=100,
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
    )
    password = forms.CharField(
        label='Password',
        max_length=100,
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'})
    )
    password_confirm = forms.CharField(
        label='Confirm Password',
        max_length=100,
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Re-enter your password'})
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        # Check if passwords match
        if password != password_confirm:
            self.add_error('password_confirm', 'Passwords do not match')

        return cleaned_data
