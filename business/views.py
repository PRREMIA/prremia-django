from django.shortcuts import render
from .models import Home

def home(request):
    home = Home.objects.filter(title='Home').first().description
    about = Home.objects.filter(title='About').first().description
    products = Home.objects.filter(title='Products').first().description

    tags = {
        '<img ': '<div class="products"><img style="width:100px;height:auto;" src="',
        '></img>': '"></img>',
        '<desc>': '<div class="desc">',
        '</desc>': '</div></div>',
    }
    for tag in tags:
        products = products.replace(tag,tags[tag])
    products = products.split('\n')
    return render(request, 'business/home.html', {'home':home, 'about':about,'products':products})

def donate(request):
    return render(request, 'business/donate.html')