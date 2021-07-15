from django.urls import path
from blog import views
app_name='blog'
urlpatterns = [
    path('base/',views.base,name='base'),
    path('register/',views.register_user,name='register'),
    path('add_text/',views.add_text,name='text'),
    #path('register', views.register,name='register'),
    path('user/',views.user,name='user'),
    path('',views.home,name='Home'),
    path('user_login/',views.user_login,name='user_login'),
    

]
