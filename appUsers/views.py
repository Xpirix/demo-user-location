from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

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
