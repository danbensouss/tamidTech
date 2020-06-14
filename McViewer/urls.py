from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('login', views.loginprofile, name="login"),
    path('sign-up', views.signUp, name="sign_up"),
    path('home', views.index, name="home_page"),
    path('search', views.searchResult, name="search_result"),
    path('getRelatedSearch/<str:id>', views.getRelatedSearch, name="getRelatedSearch"),
    path('edit-profile',views.editProfile, name="edit_profile"),
    path('network', views.network, name = "network"),
    path('network/<str:referral_code>', views.privateNetwork, name = "private_network"),
    path('create-network', views.createNetwork, name = "create_network"),
]