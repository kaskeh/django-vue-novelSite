from django.urls import path, re_path

from . import views

urlpatterns = [
    path('books_cates/', views.books_cates, name="books_cates"),
    path('<int:id>/', views.accounts, name="accounts"),
    path('login/', views.login, name="login_account"),
    path('register/', views.register, name="register_account"),
    path('token/', views.token, name="token"),
]