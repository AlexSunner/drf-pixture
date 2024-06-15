from django.db import models
from django.contrib.auth.models import User

class AdminLog(models.Model):
    admin_user = models.ForeignKey(User, related_name='admin_logs', on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    model_affected = models.CharField(max_length=255)
    object_id = models.IntegerField()

    def __str__(self):
        return f'{self.admin_user.username} performed {self.action} on {self.model_affected} ({self.object_id}) at {self.timestamp}'
