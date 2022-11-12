from django.shortcuts import render


def home(request):
    return render(request, 'home/index.html', {
        'page_title': 'Home'
    })


def about(request):
    return render(request, 'home/about.html', {
        'page_title': 'About'
    })


def blog(request):
    return render(request, 'home/blog.html', {
        'page_title': 'Blog'
    })


def contact(request):
    return render(request, 'home/contact.html', {
        'page_title': 'Contact'
    })


