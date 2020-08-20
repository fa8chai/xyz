from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login, authenticate
from .forms import CustomUserCreationForm, LoginForm
from .models import CustomUser
from home.views import main
from user_profile.views import profile
User = CustomUser


def signin(request):
    form = LoginForm()
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, phone=request.POST['phone_1'], password=request.POST['password'])
            if user:
                login(request, user)
                return redirect('main')
            else:
                try:
                    user = User.objects.get(phone=request.POST['phone_1'])
                except User.DoesNotExist:
                    return render(request, 'users/login.html', {'form':form,'error':"This phone number does't belong to an account"})
                return render(request, 'users/login.html', {'form':form,'error':"Invalid Credentials"})
        return render(request, 'users/login.html', {'form':form,'error':'Something went wrong!'})
    return render(request, 'users/login.html', {'form':form,})

def signup(request):
    form = CustomUserCreationForm
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'users/signup.html',{'form':form,})
    return render(request, 'users/signup.html',{'form':form,})



@login_required
def signout(request):
    logout(request)
    return redirect(signin)