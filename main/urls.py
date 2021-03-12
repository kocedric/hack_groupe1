from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('intern/', views.innerPage, name='innerPage'),
    path('portfolio/', views.portfolio, name='portfolio'),
]
