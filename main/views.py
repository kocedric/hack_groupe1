from django.shortcuts import render

from .models import Portfolio


def home(request):
    portfolios = Portfolio.objects.all()
    context = {'portfolios': portfolios}
    return render(request, 'main/index.html', context)


def innerPage(request):
    return render(request, 'main/inner-page.html')


def portfolio(request):
    portfolios = Portfolio.objects.all()
    context = {'portfolios': portfolios}
    return render(request, 'main/portfolio-details.html', context)
