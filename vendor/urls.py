from django.urls import path, include
from . import views
from accounts import views as AccountViews
from vendor.views import menu_builder


urlpatterns = [
    path('', AccountViews.vendorDashboard, name='vendor'),
    path('profile/', views.vprofile, name='vprofile'),
    path('menu-builder/', views.menu_builder, name='menu_builder'),
    path('menu-builde/category/<int:pk>/', views.fooditems_by_category, name='fooditems_by_category'),

    # Category CRUD-
    path('menu-builder/category/add', views.add_category, name='add_category'),
    path('menu-builder/category/edit/<int:pk>/', views.edit_category, name='edit_category'),
    path('menu-builder/category/delete/<int:pk>/', views.delete_category, name='delete_category'),

    #Food CRUD
    path('menu-builde/food/add', views.add_food, name='add_food'),
    path('menu-builder/food/edit/<int:pk>/', views.edit_food, name='edit_food'),
    path('menu-builder/food/elete/<int:pk>', views.delete_food, name='delete_food'),
]
