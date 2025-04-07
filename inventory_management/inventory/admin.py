from django.contrib import admin
from .models import Equipment

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'serial_number', 'status', 'assigned_to', 'purchase_date')
    list_filter = ('type', 'status', 'purchase_date')
    search_fields = ('name', 'serial_number', 'assigned_to__username')
    date_hierarchy = 'purchase_date'
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'type', 'serial_number')
        }),
        ('Status Information', {
            'fields': ('status', 'assigned_to', 'purchase_date')
        }),
        ('Additional Details', {
            'fields': ('notes',),
            'classes': ('collapse',)
        })
    )
