from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm


def register(request):
    if request.method != 'POST':
        form = SignUpForm()
    else:
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('logs:index')
    return render(request, 'users/register.html', {'form': form})
