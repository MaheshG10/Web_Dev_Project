from django.urls import path
from . import views

urlpatterns = [
    path('', views.ItemListView.as_view(), name='item-list'),
    path('add/', views.ItemCreateView.as_view(), name='item-add'),
    path('<int:pk>/edit/', views.ItemUpdateView.as_view(), name='item-edit'),
    path('<int:pk>/delete/', views.ItemDeleteView.as_view(), name='item-delete'),
]
