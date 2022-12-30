from . import views
from django.urls import path
app_name='authentications'

urlpatterns = [

    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('form',views.form,name='form'),
    ]