
from django.urls import path
from . import views


urlpatterns = [
    path('home/',views.home, name='home'),
    path('login/',views.login,name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/',views.register,name='register'),
    path('regform/',views.regform,name='regform'),
    path('messag/',views.messag, name='messag')

]



