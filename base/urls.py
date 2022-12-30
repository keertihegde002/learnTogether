from django.urls import path
from . import views

urlpatterns = [
    path('',views.home , name="home"),
    path('room/<str:pk>/',views.room,name="room"), 
    path('create-room',views.create_room,name="create-room"),
    path('update-room/<str:pk>',views.update_room,name="update-room"),
    path('delete-room/<str:pk>',views.delete_room,name="delete-room"),
    path('login',views.loginPage,name="login"),
    path('logout',views.logoutPage,name="logout"),
    path('register',views.registerUser,name="register"),
    path('profile/<int:pk>',views.userProfile,name="user-profile"),
    path('update-user',views.updateUser,name="user-update"),

]
