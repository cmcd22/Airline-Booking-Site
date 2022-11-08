from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('flights', views.flights, name='flights'),
    path('cancel', views.cancel, name='cancel'),
    path('book', views.book, name='book'),
    path('getflightsOW', views.getflightsOW, name='getflightsOW'),
    path('getflightsR', views.getflightsR, name='getflightsR'),
    path('confirmationoneway', views.confirmationoneway, name='confirmationoneway'),
    path('confirmationreturn', views.confirmationreturn, name='confirmationreturn'),
    path('getBooking', views.getBooking, name='getBooking'),
    path('deleteBooking', views.deleteBooking, name='deleteBooking')
]
