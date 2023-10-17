from rest_framework.viewsets import ModelViewSet

from dashboard.models import Division, District
from dashboard.serializer import DivisionSerializer, DistrictSerializer


class DivisionViewSet(ModelViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer

class DistrictViewSet(ModelViewSet):
    serializer_class = DistrictSerializer
    def get_queryset(self):
        return District.objects.filter(division_id=self.kwargs['division_pk'])
    def get_serializer_context(self):
        return {'division_id': self.kwargs['division_pk']}