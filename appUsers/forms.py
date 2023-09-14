from django import forms
from .models import CustomUser

class UserProfileForm(forms.ModelForm):
    """
    Form for the user profile edition
    """
    class Meta:
        model = CustomUser
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "placeholder": "Username",
                    "class": "form-control",
                    "type": "text",
                    "id": "input-username",
                    "name": "username",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "placeholder": "E-mail",
                    "class": "form-control",
                    "type": "email",
                    "id": "input-email",
                    "name": "email_address",
                }
            ),

            "first_name": forms.TextInput(
                attrs={
                    "placeholder": "First Name",
                    "class": "form-control",
                    "type": "text",
                    "id": "input-first-name",
                    "name": "first_name",
                }
            ),

            "last_name": forms.TextInput(
                attrs={
                    "placeholder": "Last Name",
                    "class": "form-control",
                    "type": "text",
                    "id": "input-last-name",
                    "name": "last_name",
                }
            ),

            "phone": forms.TextInput(
                attrs={
                    "placeholder": "Phone Number",
                    "class": "form-control",
                    "type": "text",
                    "id": "input-phone",
                    "name": "phone",
                }
            ),

            "address": forms.TextInput(
                attrs={
                    "placeholder": "Address",
                    "class": "form-control",
                    "type": "text",
                    "id": "input-phone",
                    "name": "phone",
                }
            ),
        }

        fields = ['first_name', 'last_name', 'phone', 'address']

