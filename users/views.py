from django.shortcuts import render, redirect
from django.contrib  import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationFrom

def register(request):
    if request.method == 'POST':
        form = UserRegistrationFrom(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            hobby = form.cleaned_data.get('hobby')
            avater = form.cleaned_data.get('avater')
            form.save()
            messages.success(request, f'Your account has been created successfully!!!')
            return redirect('login')
    else:
        form = UserRegistrationFrom()
    return render(request, 'users/register.html', {'form': form})
