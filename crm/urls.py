from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView 
from . import views

app_name = "crm"
urlpatterns = [
    path('login/' , login_view.as_view() , name="login"),
    path('logout/' , views.logoutView , name='logout'),
    path('registration/' , registrationView.as_view() , name="registration"),
    path('home/' , CrmView.as_view() , name="crm-view"),
    path('home/<int:pk>/' , CrmDetailView.as_view() , name="detail"),
    path('home/<int:pk>/delete/' , DeleteCrmView.as_view() , name="delete"),
    path('home/<int:pk>/update/' , UpdateCrmView.as_view() , name='update'),
    path('new/' , CreateCrmView.as_view() , name="new"),
]