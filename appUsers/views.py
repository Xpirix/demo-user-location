from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import CustomUser
from appUsers.forms import UserProfileForm
from django.core.serializers import serialize
import json

@login_required
def profile(request):
    """
    User profile template view
    """
    user = request.user
    return render(
        request, 
        'dashboard/profile.html', 
        {'user': user, 'segment': 'profile'}
        )

@login_required
def edit_profile(request):
    """
    Edit user profile template view
    """
    msg = None
    success = False
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            success = True
            return redirect('profile')
        else:
            success = False
            msg = "Form is not valid"

    else:
        form = UserProfileForm(instance=user)

    args = {
        "form": form,
        "msg": msg,
        "success": success,
        "segment": "profile",

    }
    
    return render(request, 'dashboard/edit_profile.html', args)


@login_required
def users_map(request):
    """
    User map template view
    """
    fields = (
        'username', 
        'first_name', 
        'last_name', 
        'email', 
        'phone',
        'address',
        'location'
        )
    data = CustomUser.objects.all()
    args = {
        "segment": "users_map",
        "users": json.loads(serialize("geojson", data, fields=fields))
    }

    return render(request, 'dashboard/users_map.html', args)

