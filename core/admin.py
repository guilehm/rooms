from django.contrib import admin

from core.models import Meeting, Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'active')
    list_filter = ('active', 'date_added')
    search_fields = ('name',)
    ordering = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ('name', 'room', 'status', 'date', 'start', 'end')
    list_filter = ('room', 'status', 'date', 'date_added')
    search_fields = ('name', 'description')
    ordering = ('start',)
