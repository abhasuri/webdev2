from django.urls import path
from home import views

urlpatterns = [
    path('', views.loginpage , name='loginuser'),  
    path('home',views.homepage, name='homepage'),
    path('aboutus',views.aboutus, name='aboutus'),
    path('contactus',views.contactus, name='contactus'), 
    path('sale',views.sale, name='sale'), 
    path('settings',views.settings, name='settings'),
]