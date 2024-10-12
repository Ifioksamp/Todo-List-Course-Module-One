from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.SignUpView, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='todo/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/success/', views.SignUpSucessView, name='success_signup'),
    path('add-todo/', views.CreateTodoView, name='add_todo'),
    path('todo/<str:pk>/update/', views.UpdateTodoView, name='update_todo'),
    path('todo/<str:pk>/delete/', views.DeleteTodoView, name='delete_todo'),
]