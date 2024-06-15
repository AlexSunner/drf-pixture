from django.db.models.signals import post_save, post_delete
from django.contrib.admin.models import LogEntry
from django.dispatch import receiver
from .models import AdminLog

@receiver(post_save, sender=LogEntry)
def log_admin_action(sender, instance, **kwargs):
    AdminLog.objects.create(
        admin_user=instance.user,
        action=f'{instance.get_action_flag_display()} {instance.object_repr}',
        model_affected=instance.content_type.model,
        object_id=instance.object_id
    )

@receiver(post_delete, sender=LogEntry)
def log_admin_deletion(sender, instance, **kwargs):
    AdminLog.objects.create(
        admin_user=instance.user,
        action=f'Deleted {instance.object_repr}',
        model_affected=instance.content_type.model,
        object_id=instance.object_id
    )