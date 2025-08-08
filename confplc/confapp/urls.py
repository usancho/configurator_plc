from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница конфигурации R050 - пока работаю над ней
    path('r050/', views.r050_conf),
    # Страница конфигурации R500 - в планах разработки
    path('r500/', views.r500_conf),
    # Страница конфигурации R500s - в планах разработки
    path('r500s/', views.r500_conf),
    # Страница конфигурации AR - в планах разработки
    path('ar/', views.ar_conf),
]