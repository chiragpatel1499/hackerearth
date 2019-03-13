from django.urls import path
from . import views

urlpatterns = [
    path('', views.login1),
    path('login1/',views.login1),
    path('logout/',views.logout),
    path('auth_view/', views.auth_view),
    path('loggedin/', views.loggedin),
    path('invalidlogin/', views.invalidlogin),
    path('signUp/', views.signUp),
    path('store/',views.store),
    path('profile/',views.profile),
]
