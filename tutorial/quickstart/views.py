from .models import Status
from rest_framework import viewsets
from rest_framework import permissions
from tutorial.quickstart.serializers import StatusSerializer

class StatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Status.objects.all().order_by('time')
    serializer_class = StatusSerializer
    permission_classes = [permissions.IsAuthenticated]
