from django.urls import path
from .views import (
    signup_view, login_view, logout_view, dashboard,
    product_list, product_create, product_update, product_delete, product_detail
)

urlpatterns = [
    # Auth
    path('', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('product/<int:pk>/', product_detail, name='product_detail'),

    # Products
    path('products/', product_list, name='product_list'),
    path('products/add/', product_create, name='product_create'),
    path('products/edit/<int:pk>/', product_update, name='product_update'),
    path('products/delete/<int:pk>/', product_delete, name='product_delete'),
]
