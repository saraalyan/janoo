from django.urls import path,include
from . import views

urlpatterns = [
    path('list', views.list_book, name='list_book'),
    path('add', views.add_book, name='add_book'),
    # path('update/<str:name>/', views.update_book, name='update_book'),
    path('delete/<int:id>/', views.delete_book, name='delete_book'),
    path('details/<int:id>/', views.details_book, name='details_book')

]