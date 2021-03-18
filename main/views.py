from django.shortcuts import render

from .models import Portfolio, Presentation


def home(request):
    portfolios = Portfolio.objects.all()
    presentations = Presentation.objects.all()
    context = {'portfolios': portfolios, 'presentations': presentations}
    return render(request, 'main/index.html', context)


def innerPage(request):
    return render(request, 'main/inner-page.html')


def portfolio(request, pk):
    portfolios = Portfolio.objects.get(id=pk)
    context = {'portfolios': portfolios}
    return render(request, 'main/portfolio-details.html', context)


# def portfolio(request, pk):
#     portfolios = Portfolio.objects.get(id=pk)
#     context = {'portfolios': portfolios}
#     return render(request, 'main/portfolio-details.html', context)
