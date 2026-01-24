from django.urls import path
from . import views

app_name = 'loads'

urlpatterns = [
    path('', views.LoadListView.as_view(), name='list'),
    path('search/routes/', views.load_route_suggestions, name='route_suggestions'),
    path('create/', views.LoadCreateView.as_view(), name='create'),
    path('<int:pk>/', views.LoadDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.LoadUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.LoadDeleteView.as_view(), name='delete'),
    path('<int:pk>/status/<str:action>/', views.load_status_change, name='status_change'),
]
