from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='quiz-home'),
    path('thankyou/', views.thankyou, name='thank-you-page')
]
