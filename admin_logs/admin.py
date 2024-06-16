from django.contrib import admin
from .models import AdminLog, AuditLog

@admin.register(AdminLog)
class AdminLogAdmin(admin.ModelAdmin):
    list_display = ('admin_user', 'action', 'timestamp', 'model_affected', 'object_id')
    search_fields = ('admin_user__username', 'action', 'model_affected')
    list_filter = ('timestamp',)

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'timestamp')
    search_fields = ('user__username', 'action')
    list_filter = ('timestamp',)