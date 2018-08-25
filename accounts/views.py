from django.shortcuts import render, redirect
from .forms import RegistationForm


def signup_account(request):
    form = RegistationForm()
    if request.method == 'POST':
        form = RegistationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')
    return render(request, 'sign_up.html', {'form': form})
