from django.urls import path

#import all the vviews from views file ( we use . becoase views is in the same directory)
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('register', views.register, name="register"),
    path('login', views.my_login, name="login"),
    path('dashboard', views.dashboard, name="dashboard"),

   
]