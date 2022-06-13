from django.urls import path
from . import views

urlpatterns=[
    path('tv/',views.testView,name='tv'),
    path('home/',views.homeView,name='home'),
    path('add-order/',views.addBookView,name='addbook'),
    path('show-order/',views.showBookView,name='showbooks'),
    path('update-order/<int:pk>/',views.updateBookView,name='updatebook'),
    path('delete-order/<int:pk>/',views.deleteBookView,name='deletebook'),

    
]