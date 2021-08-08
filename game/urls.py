from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_list, name='game_list'),
    path('game/<int:pk>/', views.game_detail, name='game_detail'),
    path('game/new/', views.game_new, name='game_new'),
    path('game/<int:pk>/edit/', views.game_edit, name='game_edit'),
]
