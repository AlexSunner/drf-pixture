from rest_framework import viewsets, permissions
from .models import AuditLog
from .serializers import AuditLogSerializer
from .permissions import IsAuthenticatedAndAdminOrSuperUser

class AuditLogViewSet(viewsets.ModelViewSet):
    queryset = AuditLog.objects.all().order_by('-timestamp')
    serializer_class = AuditLogSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [IsAuthenticatedAndAdminOrSuperUser()]

    def perform_create(self, serializer):
        # Automatically set the user field to the currently authenticated user
        serializer.save(user=self.request.user)