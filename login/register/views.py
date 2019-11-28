from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.




def index(request):
    return render(request,
    'register/index.htm',
    {'title': 'Homepage'})


@login_required
def logout(request):
    logout(request)
    return render(request, "register/logout.htm")



@login_required
def profile(request):
    return render(request,
    'register/profile.htm',
    {'title': 'Profile'})



def signup(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            user = form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}, Please Log-In')
            return redirect('login')

    else:
        form = RegForm()
    return render(request, 'register/signup.htm', {'form': form, 'title': 'Signup'})