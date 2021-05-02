from django.shortcuts import render, redirect
from .models import Password
from django.contrib import messages


def ownerLogin(request):
    if request.method == 'POST':
        password = request.POST['password']

        if password == "":
            messages.info(request, 'Incomplete Information')
            return redirect("/owner")
        else:
            if Password.objects.filter(password=password).exists():
                return redirect("/owner/home")
            else:
                messages.info(request, 'Wrong Password')
                return redirect("/owner")
    else:
        return render(request, 'ownerlogin/admin_login.html')


