from django.shortcuts import render, redirect
from .models import Account
from django.contrib import messages


def loginPage(request):
    if request.method == 'POST':
        userName = request.POST['userName']
        password = request.POST['password']

        if userName == "" or password == "":
            messages.info(request, 'Incomplete Information')
            return redirect("/")
        else:
            if Account.objects.filter(user_name=userName).exists():
                if Account.objects.filter(user_name=userName).count() == Account.objects.filter(password=password).count():
                    return redirect("user/home")
                else:
                    messages.info(request, 'Wrong Password')
                    return redirect("/")
            else:
                messages.info(request, 'Invalid Account')
                return redirect("/")
    else:
        return render(request, 'loginsignup/login_page.html')


def signupPage(request):
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        emailAdd = request.POST['emailAdd']
        mobileNo = request.POST['mobileNo']
        homeAdd = request.POST['homeAdd']
        userName = request.POST['userName']
        password = request.POST['password']
        confirmation = request.POST['confirmation']

        if firstName == "" or lastName == "" or emailAdd == "" or mobileNo == "" or homeAdd == "" or userName == "" or password == "" or confirmation == "":
            messages.info(request, 'Complete All the Information')
            return redirect('/signup')
        if password == confirmation:
            if Account.objects.filter(user_name=userName).exists():
                messages.info(request, 'Username Taken')
                return redirect('/signup')
            elif Account.objects.filter(email_add=emailAdd).exists():
                messages.info(request, 'Email Taken')
                return redirect('/signup')
            else:
                account = Account.objects.create(first_name=firstName, last_name=lastName, email_add=emailAdd,
                                         mobile_no=mobileNo, home_add=homeAdd, user_name=userName, password=password)
                account.save()
                return redirect('/')
        else:
            messages.info(request, 'Password Do Not Match')
            return redirect('/signup')

    else:
        return render(request, 'loginsignup/signup_page.html')


def aboutPage(request):
    return render(request, 'loginsignup/about_page.html')