from django.urls import path

from . import views

urlpatterns = [
    path('books_cates/', views.books_cates, name="books_cates"),
    path('<int:id>/', views.accounts, name="accounts"),
]