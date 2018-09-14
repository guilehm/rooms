from django.urls import path

from core import views

app_name = 'core'


urlpatterns = [
    path('', views.index, name='index'),
    path('room/list/', views.room_list, name='room-list'),
]
