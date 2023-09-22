from django.urls import path 

from . import views 

urlpatterns = [
    path('home/',views.home , name='Home'),
    path('signup/',views.signup, name='Sign-up'),
    path('weather/',views.weather, name='Weather'),
    path('Data/',views.show, name='Data'),
]
