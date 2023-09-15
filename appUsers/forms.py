from django.contrib.gis import forms
from .models import CustomUser

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

