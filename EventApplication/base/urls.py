from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="home"),
    path('event/<str:pk>/', views.event_page, name="event"),
    path('eventconfirm/<str:pk>/', views.registration_confirmation, name="confirm"),
    path('user/<str:pk>/', views.user_page, name="userprofile"),
    path('account/<str:pk>/', views.account_page, name="account")
]
