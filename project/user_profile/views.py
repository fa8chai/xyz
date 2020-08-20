from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile
from home.views import main, overview


@login_required
def profile(request):
    user_profile = Profile.objects.get(user=request.user)
    if user_profile.user.is_superuser:
        return redirect('overview')
    form = ProfileForm(instance=user_profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            profile = form.save()
            return redirect('main')
        return render(request, 'user_profile/main.html', {'form':form,'error':'error'})
    return render(request, 'user_profile/main.html', {'form':form,})




