from .models import Division, District, Tehsil, UC, Facility, lhw_info, LHW
from .resources import (
    DivisionResource, DistrictResource, TehsilResource, UCResource,
    FacilityResource, lhw_infoResource, LHWResource
)
from .resources import SupervisionResource
from django.contrib import admin
from .models import District, Division, Supervision
from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import MotherHealth, FamilyPlanning, BirthsDeaths
from .resources import MotherHealthResource, FamilyPlanningResource, BirthsDeathsResource



# myapp/admin.py

from django.contrib import admin
from import_export.admin import ImportExportMixin, ImportMixin, ExportActionMixin

from .models import ChildHealth
from .resources import ChildHealthResource


admin.site.site_header = "Intellegent and Customizeable Dashboard"
admin.site.site_title = "Intellegent and Customizeable Dashboard"

class ChildHealthAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = ChildHealthResource
    list_display = ['lhw_code',
        'no_newborns_weighted',
        'no_low_birth_weight_babies',
        'no_newborn_started_breast_feeding',
        'no_newborn_applied_chlorhexidine',
        'no_newborn_immunization_started',
        'no_6_months_old_children',
        'no_6_months_old_children_exclusive_breast_feeding',
        'no_6_59_months_old_children',
        'no_6_59_months_old_children_mauc_done',
        'no_6_59_months_children_malnutrition_mauc',
        'no_6_59_months_children_malnutrition_less_than_mauc',
        'no_12_23_months_old_children',
        'no_12_23_months_old_children_fully_immunized',
        'no_5_years_children',
        'no_5_years_children_micro_nutrition_sachet',
        'no_5_years_children_gm_done_recorded',
        'no_5_years_children_low_weight',]
    list_filter = [
        'no_newborns_weighted',
        'no_low_birth_weight_babies',
        'no_newborn_started_breast_feeding',
        'no_newborn_applied_chlorhexidine',
        'no_newborn_immunization_started',
        'no_6_months_old_children',
        'no_6_months_old_children_exclusive_breast_feeding',
        'no_6_59_months_old_children',
        'no_6_59_months_old_children_mauc_done',
        'no_6_59_months_children_malnutrition_mauc',
        'no_6_59_months_children_malnutrition_less_than_mauc',
        'no_12_23_months_old_children',
        'no_12_23_months_old_children_fully_immunized',
        'no_5_years_children',
        'no_5_years_children_micro_nutrition_sachet',
        'no_5_years_children_gm_done_recorded',
        'no_5_years_children_low_weight',
    ]


    # Add other fields as needed

admin.site.register(ChildHealth, ChildHealthAdmin)


class MotherHealthAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'lhw_code',
        'no_newly_registered_pregnant_women',
        'total_pregnant_women',
        'total_pregnant_women_visited',
        'no_pregnant_breastfeeding_women_mauc_done',
        'no_pregnant_breastfeeding_malnutrition_women_mauc',
        'no_pregnant_women_supplied_iron_tablets',
        'no_abortions',
        'total_deliveries',
        'no_women_delivered_provided_misoprostol',
        'no_women_delivered_anc_visits_by_sbas',
        'no_women_delivered_tt_completed_before_delivery',
        'no_deliveries_by_skilled_birth_attendants',
        'no_postnatal_cases_visited_within_24_hours',
    ]
    list_filter = [
        'total_pregnant_women_visited',
        'no_pregnant_breastfeeding_women_mauc_done',
        'no_deliveries_by_skilled_birth_attendants',
    ]

admin.site.register(MotherHealth, MotherHealthAdmin)
class FamilyPlanningAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = FamilyPlanningResource
    list_display = [
        'lhw_code',
        'no_eligible_couples',
        'no_new_clients_family_planning',
        'no_followup_cases_family_planning',
        'total_traditional_method_users',
        'total_modern_contraceptive_users',
        'no_condom_users',
        'no_oral_pills_users',
        'no_coc_users',
        'no_ecp_users',
        'no_injectable_contraceptive_users',
        'no_2_month_injection',
        'no_3_month_injection',
        'no_iucd_clients',
        'no_surgical_clients',
        'no_other_modern_contraceptive_users',
        'no_clients_referred',
        'no_clients_supplied_condoms',
        'no_clients_supplied_oral_pills',
        'no_clients_administered_injectable_contraceptives',
    ]
    list_filter = [
        'no_eligible_couples',
        'total_modern_contraceptive_users',
        'no_clients_referred',
    ]


class BirthsDeathsAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = BirthsDeathsResource
    list_display = [
        'no_live_births',
        'no_still_births',
        'no_all_deaths',
        'no_neonatal_deaths',
        'no_infant_deaths_week',
        'no_infant_deaths_month',
        'no_children_deaths',
        'no_maternal_deaths',
    ]
    list_filter = [
        'no_live_births',
        'no_still_births',
        'no_all_deaths',
        'no_neonatal_deaths',
        'no_infant_deaths_week',
        'no_infant_deaths_month',
        'no_children_deaths',
        'no_maternal_deaths',
    ]

admin.site.register(FamilyPlanning, FamilyPlanningAdmin)
admin.site.register(BirthsDeaths, BirthsDeathsAdmin)

class SupervisionAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = SupervisionResource
    list_display = [
        'lhw_code',
        'no_of_visits_by_lhs',
        'no_of_visits_by_dco_np',
        'no_of_visits_by_adc_np',
        'no_of_visits_by_fpo',
        'no_of_visits_by_ppiu',
    ]
    list_filter = [
        'no_of_visits_by_lhs',
        'no_of_visits_by_dco_np',
        'no_of_visits_by_adc_np',
        'no_of_visits_by_fpo',
        'no_of_visits_by_ppiu',
    ]

class DivisionAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['division']
    list_filter = ['division']

class DistrictAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['district', 'division']
    list_filter = ['district', 'division']

class TehsilAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['tehsil', 'district']
    list_filter = ['tehsil', 'district']

class UCAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['uc', 'tehsil']
    list_filter = ['uc', 'tehsil']

class FacilityAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['facility', 'district', 'tehsil', 'uc', 'area_type_id', 'population']
    list_filter = ['district', 'tehsil', 'uc', 'area_type_id']

class lhw_infoAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['name', 'uc', 'facility']
    list_filter = ['uc', 'facility']

class LHWAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'lhw_code', 'lhw_name', 'lhw_cnic', 'lhw_father_husband_name',
        'lhw_attached_facility', 'lhw_union_council', 'lhw_tehsil',
        'lhw_district', 'catchment_population_flcf', 'population_registered_by_lhws',
    ]
    list_filter = [ 'lhw_union_council', 'lhw_tehsil', 'lhw_district']


admin.site.register(Supervision, SupervisionAdmin)
admin.site.register(Division, DivisionAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Tehsil, TehsilAdmin)
admin.site.register(UC, UCAdmin)
admin.site.register(Facility, FacilityAdmin)
admin.site.register(lhw_info, lhw_infoAdmin)
admin.site.register(LHW, LHWAdmin)
# Register your models here.
