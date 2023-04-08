# from django.contrib import admin
from django.urls import path,include
from.views import CartNew
urlpatterns = [
    path('cart-items/', CartNew.as_view()),
]