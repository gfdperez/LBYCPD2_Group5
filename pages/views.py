from django.shortcuts import render
from .models import Drink


def homePage(request):
    return render(request, 'pages/home_page.html', {'title': 'Home'})


def menuPage(request):
    drink1 = Drink()
    drink1.name = 'PENGU'
    drink1.subname = 'MILK MILKTEA'
    drink1.price_medium = 79
    drink1.price_large = 89
    drink1.image = 'PENGU MILK.png'
    drink1.bgcolor = 'item1'

    drink2 = Drink()
    drink2.name = 'ROYAL'
    drink2.subname = 'OKI-OKI'
    drink2.price_medium = 89
    drink2.price_large = 99
    drink2.image = 'ROYAL OKI.png'
    drink2.bgcolor = 'item2'

    drink3 = Drink()
    drink3.name = 'EMPEROR'
    drink3.subname = 'CREAMCHEESE OREO'
    drink3.price_medium = 99
    drink3.price_large = 109
    drink3.image = 'EMPEROR.png'
    drink3.bgcolor = 'item3'

    drink4 = Drink()
    drink4.name = 'GENTOO'
    drink4.subname = 'CARAMEL CREME'
    drink4.price_medium = 99
    drink4.price_large = 109
    drink4.image = 'GENTOO CARAMEL.png'
    drink4.bgcolor = 'item4'

    drink5 = Drink()
    drink5.name = 'ROCKHOPPER'
    drink5.subname = 'WINTERMELON MILK'
    drink5.price_medium = 99
    drink5.price_large = 109
    drink5.image = 'ROCKHOPPER WM.png'
    drink5.bgcolor = 'item5'

    drink6 = Drink()
    drink6.name = 'VANILLA'
    drink6.subname = 'CRUMBLE DELUXE'
    drink6.price_medium = 99
    drink6.price_large = 109
    drink6.image = 'VANILLA CRUMBLE.png'
    drink6.bgcolor = 'item6'

    drink7 = Drink()
    drink7.name = 'ADELIE'
    drink7.subname = 'BERRY APOLLO'
    drink7.price_medium = 99
    drink7.price_large = 119
    drink7.image = 'ADELIE BERRY.png'
    drink7.bgcolor = 'item7'

    drink8 = Drink()
    drink8.name = 'MATCHA'
    drink8.subname = 'SUPREME'
    drink8.price_medium = 99
    drink8.price_large = 119
    drink8.image = 'MATCHA SUPREME.png'
    drink8.bgcolor = 'item8'

    drink9 = Drink()
    drink9.name = 'FAIRY'
    drink9.subname = 'LYCHEE'
    drink9.price_medium = 75
    drink9.price_large = 85
    drink9.image = 'FAIRY LYCHEE.png'
    drink9.bgcolor = 'item9'

    drink10 = Drink()
    drink10.name = 'FAIRY'
    drink10.subname = 'LYCHEE YAKULT'
    drink10.price_medium = 89
    drink10.price_large = 99
    drink10.image = 'FAIRY YAKULT.png'
    drink10.bgcolor = 'item10'

    drink11 = Drink()
    drink11.name = 'KING'
    drink11.subname = 'CHOCO MILK'
    drink11.price_medium = 89
    drink11.price_large = 99
    drink11.image = 'KING CHOCO.png'
    drink11.bgcolor = 'item11'

    drink12 = Drink()
    drink12.name = 'KING'
    drink12.subname = 'CHUNKY CHOCO'
    drink12.price_medium = 99
    drink12.price_large = 109
    drink12.image = 'KING CHUNKY.png'
    drink12.bgcolor = 'item12'

    drinks = [drink1, drink2, drink3, drink4, drink5, drink6, drink7, drink8, drink9, drink10, drink11, drink12]

    return render(request, 'pages/menu_page.html', {'drinks': drinks, 'title': 'Menu'})
