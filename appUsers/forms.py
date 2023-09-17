from django.contrib.gis import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UserProfileForm(forms.ModelForm):
    """
    Form for the user profile edition
    """
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'phone', 'address', 'location']

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    phone = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    address = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    location = forms.PointField(
        widget=forms.OSMWidget(attrs={
            'map_width': '100%', 
            'map_height': 500})
    )



class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control",
                "autocomplete": "off",
            }
        ))
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "First Name",
                "autocomplete": "off",
                "class": "form-control"
            }
        ))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last Name",
                "autocomplete": "off",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "autocomplete": "off",
                "class": "form-control"
            }
        ))
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Phone Number",
                "autocomplete": "off",
                "class": "form-control"
            }
        )
    )
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Address",
                "autocomplete": "off",
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "autocomplete": "off",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm Password",
                "autocomplete": "off",
                "class": "form-control"
            }
        ))
    location = forms.PointField(
        widget=forms.OSMWidget(attrs={
            'map_width': '100%', 
            'map_height': 300})
    )

    def clean(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError({"email": "Email exists"})

        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError({"username": "Username exists"})

        password = self.cleaned_data.get('password1')
        password1 = self.cleaned_data.get('password2')
        if password != password1:
            raise ValidationError(
                {
                    "password1": "Password and confirm password do not match",
                    "password2": "Password and confirm password do not match"
                }
            )
        return self.cleaned_data

    class Meta:
        model = CustomUser
        fields = (
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'phone', 
            'address', 
            'password1', 
            'password2',
            'location'
        )

