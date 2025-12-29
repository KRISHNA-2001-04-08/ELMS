from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Leave
from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('apply/')
    return render(request, 'login.html')



def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        User.objects.create_user(username=username, password=password)
        return redirect('/')   # go to login after signup

    return render(request, 'signup.html')

@login_required
def apply_leave(request):
    if request.method == 'POST':
        Leave.objects.create(
            user=request.user,
            reason=request.POST['reason'],
            from_date=request.POST['from_date'],
            to_date=request.POST['to_date']
        )
        return redirect('my_leaves')
    return render(request, 'apply_leave.html')

@login_required
def my_leaves(request):
    leaves = Leave.objects.filter(user=request.user)
    return render(request, 'my_leaves.html', {'leaves': leaves})

@login_required
def manage_leaves(request):
    leaves = Leave.objects.all()
    return render(request, 'manage_leaves.html', {'leaves': leaves})

@login_required
def update_status(request, id, status):
    leave = Leave.objects.get(id=id)
    leave.status = status
    leave.save()
    return redirect('manage_leaves')