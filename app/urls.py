from django.urls import path
from app.views import app
from app import views  # Импорт из приложения app

urlpatterns = [
    path('', app, name='app'),
    path('banners/', views.banner_list, name='banner_list'),
]
