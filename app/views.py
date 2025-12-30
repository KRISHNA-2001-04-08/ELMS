from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Leave
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)

            # 🔑 ROLE BASED REDIRECT
            if user.is_superuser:
                return redirect('manage_leaves')   # admin
            else:
                return redirect('apply_leave')    # normal user

    return render(request, 'login.html')



@login_required
@user_passes_test(lambda u: u.is_superuser)
def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        User.objects.create_user(username=username, password=password)
        return redirect('manage_leaves')

    return render(request, 'signup.html')


@login_required
@user_passes_test(lambda u: not u.is_superuser)
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
@user_passes_test(lambda u: not u.is_superuser)
def my_leaves(request):
    leaves = Leave.objects.filter(user=request.user)
    return render(request, 'my_leaves.html', {'leaves': leaves})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def manage_leaves(request):
    leaves = Leave.objects.all()
    return render(request, 'manage_leaves.html', {'leaves': leaves})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def update_status(request, id, status):
    leave = Leave.objects.get(id=id)
    leave.status = status
    leave.save()
    return redirect('manage_leaves')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


