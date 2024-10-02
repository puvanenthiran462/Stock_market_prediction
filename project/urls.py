
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('asd/',views.asd,name='asd'),
    path('Google_price/',views.Google_price,name='Google_price'),
    path('select/',views.select,name='select')
]
