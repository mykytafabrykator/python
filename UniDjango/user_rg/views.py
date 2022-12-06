from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                usern = form.cleaned_data.get('username')
                messages.success(request, f'Account was created for {usern}')
                return redirect('login')

        context = {'form': form}
        return render(request, 'user_rg/register.html', context)