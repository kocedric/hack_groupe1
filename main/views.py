from django.shortcuts import render


def home(request):
    return render(request, 'main/index.html')


def innerPage(request):
    return render(request, 'main/inner-page.html')


def portfolio(request):
    return render(request, 'main/portfolio-details.html')
