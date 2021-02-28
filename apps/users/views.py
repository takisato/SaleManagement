from django.shortcuts import render,redirect
from .form import CustomUserForm


def user_new(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')
        else:
            return render(request, 'users/user_new.html', {'form': form})

    else:
        form = CustomUserForm()
    return render(request, 'users/user_new.html', {'form': form})