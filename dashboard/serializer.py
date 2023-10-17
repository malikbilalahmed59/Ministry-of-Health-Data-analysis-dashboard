from rest_framework import serializers
from .models import Division, District, Tehsil, UC, Facility, lhw_info


class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'


class TehsilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tehsil
        fields = '__all__'


class UCSerializer(serializers.ModelSerializer):
    class Meta:
        model = UC
        fields = '__all__'


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = '__all__'


class lhw_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = lhw_info
        fields = '__all__'
