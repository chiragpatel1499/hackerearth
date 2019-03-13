from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home),
    path('display_data/',views.display_data),
    path('sort_column/',views.sort_column),
    path('filter_By_Country', views.filter_By_Country),
    path('filter_By_Province', views.filter_By_Province),
    path('filter_By_Region_1', views.filter_By_Region_1),
    path('filter_By_Region_2', views.filter_By_Region_2),
    path('',views.home),

]