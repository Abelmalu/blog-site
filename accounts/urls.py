from django.urls import path
from . import views 

from . import views
# Create your tests here.

# app_name= 'accounts'

urlpatterns =[
    path('',views.signup_view, name="signup"),
 
    path('login/',views.login_view, name="login"),
    path('logout/',views.logout_view, name="logout"),
 
]