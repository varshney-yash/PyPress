from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import UserRegForm

def register(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created! Welcome, {username}")
            return redirect('blog-home')
        else:
            for error in form.non_field_errors():
                messages.error(request, error)
            for field in form.errors:
                for error in form.errors[field]:
                    messages.error(request, error)
    else:
        form = UserRegForm()
    return render(request, 'users/register.html', {'form' : form})

def login(request):
    pass