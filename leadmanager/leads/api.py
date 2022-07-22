from leads.models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer

#lead viewset  create read update delete crud requests
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes= [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer