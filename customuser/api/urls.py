from django.urls import path
from api import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('change-password/', views.password_change, name="passwordchange"),   
    path('set-new-password/', views.set_new_password, name="setnewpassword"),       
    path('login/', views.login_user, name="login_user"),           
    path('logout/', views.logout_user, name="logout_user"),               
    path('', views.index, name="home"),
]