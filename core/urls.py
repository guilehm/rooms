from django.urls import path

from core import views

app_name = 'core'


urlpatterns = [
    path('', views.index, name='index'),
    path('room/list/', views.room_list, name='room-list'),
    path('room/add/', views.room_add, name='room-add'),
    path('room/<int:room_id>/change/', views.room_change, name='room-change'),
    path('meeting/list/', views.meeting_list, name='meeting-list'),
    path('meeting/add/', views.meeting_add, name='meeting-add'),
    path('meeting/<int:meeting_id>/change/', views.meeting_change, name='meeting-change'),
    path('meeting/calendar/', views.meeting_calendar, name='meeting-calendar'),
]
