from django.urls import path

from. import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_item, name='add'),
    path('shopping_list/', views.shopping_list, name='shopping_list'),
    # path('edit/<int:id>/', views.edit, name='edit'),
    ]