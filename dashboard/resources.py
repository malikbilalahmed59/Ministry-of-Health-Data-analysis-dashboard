# myapp/resources.py

from import_export import resources

from .models import ChildHealth
from .models import Supervision
from .models import Division, District, Tehsil, UC, Facility, lhw_info, LHW
from .models import MotherHealth, FamilyPlanning, BirthsDeaths

class SupervisionResource(resources.ModelResource):
    class Meta:
        model = Supervision
class ChildHealthResource(resources.ModelResource):
    class Meta:
        model = ChildHealth

class MotherHealthResource(resources.ModelResource):
    class Meta:
        model = MotherHealth

class FamilyPlanningResource(resources.ModelResource):
    class Meta:
        model = FamilyPlanning

class BirthsDeathsResource(resources.ModelResource):
    class Meta:
        model = BirthsDeaths


class DivisionResource(resources.ModelResource):
    class Meta:
        model = Division

class DistrictResource(resources.ModelResource):
    class Meta:
        model = District

class TehsilResource(resources.ModelResource):
    class Meta:
        model = Tehsil

class UCResource(resources.ModelResource):
    class Meta:
        model = UC

class FacilityResource(resources.ModelResource):
    class Meta:
        model = Facility

class lhw_infoResource(resources.ModelResource):
    class Meta:
        model = lhw_info

class LHWResource(resources.ModelResource):
    class Meta:
        model = LHW