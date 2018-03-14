from django.shortcuts import render
from .models import User
from .forms import NewUserForm


def index(request):
    return render(request, 'users_app/index.html')


def users(request):
    form = NewUserForm()

    if request.method == 'POST':
        print(request.POST)
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Invalid Form')

    return render(request, 'users_app/users.html', {'form': form})
