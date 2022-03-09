from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter()

router.register('battles_create', views.BattleCreateViewSet, basename='create_battle')
router.register('battles_list', views.BattleListViewSet, basename='battles_list')
router.register('/battles/accept', views.BattleAcceptViewSet, basename='accpet_battle')
router.register('battles_start', views.StartBattleViewSet, basename='battles_start')
router.register('battles_move', views.BattleMoveViewSet, basename='battles_move')
router.register('battles_finish', views.CompleteBattleViewSet, basename='complete_battle')

urlpatterns = [
    path('', include(router.urls)),
]