from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logut, name='logout'),
    path('profile', views.profile, name='profile'),
    path('adminsite', views.adminsite, name='adminsite'),
    path('update', views.update, name='update'),

]
