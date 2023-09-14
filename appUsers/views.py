from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse

from appUsers.forms import UserProfileForm

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
            return redirect('profile')
        else:
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


@login_required(login_url="/")
def users_map(request):
    
    args = {
        "segment": "users_map",

    }
    return render(request, 'dashboard/users_map.html', args)