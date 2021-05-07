from django.shortcuts import render, redirect
from .models import Drink
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth import get_user_model, login


def homePage(request):
    return render(request, 'pages/home_page.html', {'title': 'Home'})


def menuPage(request):
    drinks = Drink.objects.all()
    return render(request, 'pages/menu_page.html', {'drinks': drinks, 'title': 'Menu'})


def accountPage(request):
    MyUser = request.user
    return render(request, 'pages/account_page.html', {'title': MyUser.first_name})


def signOut(request):
    auth.logout(request)
    return redirect("/")


def settingsPage(request):
    MyUser = request.user
    Accounts = get_user_model()
    if request.method == 'POST':
        firstName = request.POST['fnType']
        lastName = request.POST['lnType']
        username = request.POST['unType']
        currPass = request.POST['pValue']
        newPass = request.POST['pType']
        confirmPass = request.POST['confirmPType']
        emailAdd = request.POST['emailType']
        mobileNo = request.POST['numType']
        homeAdd = request.POST['addType']

        if firstName != "":
            MyUser.first_name = firstName
        if lastName != "":
            MyUser.last_name = lastName
        if username != "":
            if Accounts.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('/user/myAccount/settings')
            else:
                MyUser.username = username
        if emailAdd != "":
            if Accounts.objects.filter(email=emailAdd).exists():
                messages.info(request, 'Email Taken')
                return redirect('/user/myAccount/settings')
            else:
                MyUser.email = emailAdd
        if mobileNo != "":
            if len(mobileNo) != 11:
                messages.info(request, 'Invalid Contact Number')
                return redirect('/user/myAccount/settings')
            else:
                MyUser.mobile_no = mobileNo
        if homeAdd != "":
            MyUser.home_add = homeAdd
        if currPass != "":
            if MyUser.check_password(currPass):
                if newPass == confirmPass:
                    if Accounts.objects.filter(password=newPass).exists():
                        messages.info(request, 'Password Taken')
                        return redirect('/user/myAccount/settings')
                    else:
                        MyUser.set_password(newPass)
                else:
                    messages.info(request, 'Passwords Do Not Match')
                    return redirect('/user/myAccount/settings')
            else:
                messages.info(request, 'Incorrect Current Password')
                return redirect('/user/myAccount/settings')
        MyUser.save()
        login(request, MyUser)
        return render(request, 'pages/account_page.html', {'title': MyUser.first_name})

    else:
        return render(request, 'pages/settings_page.html', {'title': MyUser.first_name})


