from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
	actions_on_top = False
	actions_on_bottom = True
	empty_value_display = '-empty-'
	list_display_links = ('name',)
	list_display = ('id', 'name', 'institute', 'idno', 'phone', 'can_solve', 'dept', 'psrn')
	search_fields = ('name', 'idno')
	list_filter = ('institute', 'can_solve',)

@admin.register(BITSians)
class BITSianAdmin(admin.ModelAdmin):
	actions_on_top = False
	actions_on_bottom = True
	empty_value_display = '-empty-'
	list_display = ('name', 'idno', 'hostel', 'room', 'email', 'registered')
	search_fields = ('name', 'idno', 'room')
	list_filter = ('hostel', 'registered',)
	readonly_fields = ('idno', 'email', 'registered')