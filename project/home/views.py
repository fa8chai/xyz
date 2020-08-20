from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import CustomUser as User

@login_required
def main(request):
    if request.user.is_superuser:
        return redirect('overview')
    context={
        'user':request.user
    }
    return render(request, 'home/main.html', context=context)


@login_required
def overview(request):
    try:
        users = User.objects.all().exclude(phone=request.user.phone)
    except User.DoesNotExist:
        users = None
    if users:
        context={
            'users':users
        }
        return render(request, 'home/overview.html', context=context)
    return render(request, 'home/overview.html',{})