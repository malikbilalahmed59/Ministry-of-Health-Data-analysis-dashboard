from django.db import models


class Division(models.Model):
    division = models.CharField(max_length=255)

    def __str__(self):
        return self.division


class District(models.Model):
    district = models.CharField(max_length=255)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)

    def __str__(self):
        return self.district


class Tehsil(models.Model):
    tehsil = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.tehsil


class UC(models.Model):
    uc = models.CharField(max_length=255)
    tehsil = models.ForeignKey(Tehsil, on_delete=models.CASCADE)

    def __str__(self):
        return self.uc


class Facility(models.Model):
    facility = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    tehsil = models.ForeignKey(Tehsil, on_delete=models.CASCADE)
    uc = models.ForeignKey(UC, on_delete=models.CASCADE)
    area_type_id = models.PositiveIntegerField(null=True, blank=True)
    population = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.facility


class lhw_info(models.Model):
    name = models.CharField(max_length=255)
    uc = models.ForeignKey(UC, on_delete=models.CASCADE)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class LHW(models.Model):
    lhw_code = models.CharField(max_length=20, unique=True)
    lhw_name = models.CharField(max_length=255)
    lhw_cnic = models.CharField(max_length=15, unique=True)
    lhw_father_husband_name = models.CharField(max_length=255)
    lhw_attached_facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    lhw_union_council = models.ForeignKey(UC, on_delete=models.CASCADE)
    lhw_tehsil = models.ForeignKey(Tehsil, on_delete=models.CASCADE)
    lhw_district = models.ForeignKey(District, on_delete=models.CASCADE)
    catchment_population_flcf = models.PositiveIntegerField()
    population_registered_by_lhws = models.PositiveIntegerField()

    def __str__(self):
        return self.lhw_code


class BasicInformation(models.Model):
    lhw_code = models.ForeignKey(
        LHW,
        on_delete=models.CASCADE,
        related_name='basic_information'
    )
    is_health_committees_formulated = models.BooleanField(verbose_name="Is Health Committees Formulated", default=False)
    is_women_support_groups_formulated = models.BooleanField(verbose_name="Is Women Support Groups Formulated",
                                                             default=False)
    household_registered_by_lhws = models.PositiveIntegerField(verbose_name="Household Registered by LHWs", default=0)
    household_using_iodine_salt = models.PositiveIntegerField(verbose_name="Household Using Iodine Salt", default=0)


class HouseholdWithDrinkingWaterSource(models.Model):
    basic_info = models.ForeignKey(BasicInformation, on_delete=models.CASCADE)
    tap = models.PositiveIntegerField(verbose_name="Tap (Public Health - Engineering)", default=0)
    hand_pump = models.PositiveIntegerField(verbose_name="Hand Pump / Motor Pump", default=0)
    spring = models.PositiveIntegerField(verbose_name="Spring", default=0)
    well = models.PositiveIntegerField(verbose_name="Well", default=0)
    other = models.PositiveIntegerField(verbose_name="Other", default=0)
    total = models.PositiveIntegerField(verbose_name="Total", default=0)


class SewerageSystem(models.Model):
    basic_info = models.ForeignKey(BasicInformation, on_delete=models.CASCADE)
    pit = models.PositiveIntegerField(verbose_name="Pit", default=0)
    flush_system = models.PositiveIntegerField(verbose_name="Flush System", default=0)
    open_fields = models.PositiveIntegerField(verbose_name="Open Fields", default=0)
    total = models.PositiveIntegerField(verbose_name="Total", default=0)


class SocialContacts(models.Model):
    lhw_code = models.ForeignKey(
        lhw_info,
        on_delete=models.CASCADE,
        related_name='social_contacts'
    )
    no_health_committee_meetings = models.PositiveIntegerField(default=0)
    no_women_support_group_meetings = models.PositiveIntegerField(default=0)
    no_health_education_sessions_in_school = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "Social Contacts"


class ChildHealth(models.Model):
    lhw_code = models.ForeignKey(
        lhw_info,
        on_delete=models.CASCADE,
        related_name='child_health'
    )
    no_newborns_weighted = models.PositiveIntegerField(default=0)
    no_low_birth_weight_babies = models.PositiveIntegerField(default=0)
    no_newborn_started_breast_feeding = models.PositiveIntegerField(default=0)
    no_newborn_applied_chlorhexidine = models.PositiveIntegerField(default=0)
    no_newborn_immunization_started = models.PositiveIntegerField(default=0)
    no_6_months_old_children = models.PositiveIntegerField(default=0)
    no_6_months_old_children_exclusive_breast_feeding = models.PositiveIntegerField(default=0)
    no_6_59_months_old_children = models.PositiveIntegerField(default=0)
    no_6_59_months_old_children_mauc_done = models.PositiveIntegerField(default=0)
    no_6_59_months_children_malnutrition_mauc = models.PositiveIntegerField(default=0)
    no_6_59_months_children_malnutrition_less_than_mauc = models.PositiveIntegerField(default=0)
    no_12_23_months_old_children = models.PositiveIntegerField(default=0)
    no_12_23_months_old_children_fully_immunized = models.PositiveIntegerField(default=0)
    no_5_years_children = models.PositiveIntegerField(default=0)
    no_5_years_children_micro_nutrition_sachet = models.PositiveIntegerField(default=0)
    no_5_years_children_gm_done_recorded = models.PositiveIntegerField(default=0)
    no_5_years_children_low_weight = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "Child Health"


class MotherHealth(models.Model):
    lhw_code = models.ForeignKey(
        lhw_info,
        on_delete=models.CASCADE,
        related_name='mother_health'
    )
    no_newly_registered_pregnant_women = models.PositiveIntegerField(default=0)
    total_pregnant_women = models.PositiveIntegerField(default=0)
    total_pregnant_women_visited = models.PositiveIntegerField(default=0)
    no_pregnant_breastfeeding_women_mauc_done = models.PositiveIntegerField(default=0)
    no_pregnant_breastfeeding_malnutrition_women_mauc = models.PositiveIntegerField(default=0)
    no_pregnant_women_supplied_iron_tablets = models.PositiveIntegerField(default=0)
    no_abortions = models.PositiveIntegerField(default=0)
    total_deliveries = models.PositiveIntegerField(default=0)
    no_women_delivered_provided_misoprostol = models.PositiveIntegerField(default=0)
    no_women_delivered_anc_visits_by_sbas = models.PositiveIntegerField(default=0)
    no_women_delivered_tt_completed_before_delivery = models.PositiveIntegerField(default=0)
    no_deliveries_by_skilled_birth_attendants = models.PositiveIntegerField(default=0)
    no_postnatal_cases_visited_within_24_hours = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "Mother Health"


class FamilyPlanning(models.Model):
    lhw_code = models.ForeignKey(
        lhw_info,
        on_delete=models.CASCADE,
        related_name='family_planning'
    )
    no_eligible_couples = models.PositiveIntegerField(default=0)
    no_new_clients_family_planning = models.PositiveIntegerField(default=0)
    no_followup_cases_family_planning = models.PositiveIntegerField(default=0)
    total_traditional_method_users = models.PositiveIntegerField(default=0)
    total_modern_contraceptive_users = models.PositiveIntegerField(default=0)
    no_condom_users = models.PositiveIntegerField(default=0)
    no_oral_pills_users = models.PositiveIntegerField(default=0)
    no_coc_users = models.PositiveIntegerField(default=0)
    no_ecp_users = models.PositiveIntegerField(default=0)
    no_injectable_contraceptive_users = models.PositiveIntegerField(default=0)
    no_2_month_injection = models.PositiveIntegerField(default=0)
    no_3_month_injection = models.PositiveIntegerField(default=0)
    no_iucd_clients = models.PositiveIntegerField(default=0)
    no_surgical_clients = models.PositiveIntegerField(default=0)
    no_other_modern_contraceptive_users = models.PositiveIntegerField(default=0)
    no_clients_referred = models.PositiveIntegerField(default=0)
    no_clients_supplied_condoms = models.PositiveIntegerField(default=0)
    no_clients_supplied_oral_pills = models.PositiveIntegerField(default=0)
    no_clients_administered_injectable_contraceptives = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "Family Planning"


class BirthsDeaths(models.Model):
    lhw_code = models.ForeignKey(
        lhw_info,
        on_delete=models.CASCADE,
        related_name='birth_deaths'
    )
    no_live_births = models.PositiveIntegerField(default=0)
    no_still_births = models.PositiveIntegerField(default=0)
    no_all_deaths = models.PositiveIntegerField(default=0)
    no_neonatal_deaths = models.PositiveIntegerField(default=0)
    no_infant_deaths_week = models.PositiveIntegerField(default=0)
    no_infant_deaths_month = models.PositiveIntegerField(default=0)
    no_children_deaths = models.PositiveIntegerField(default=0)
    no_maternal_deaths = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "Births and Deaths"


class Supervision(models.Model):
    lhw_code = models.ForeignKey(
        lhw_info,
        on_delete=models.CASCADE,
        related_name='supervision'
    )
    no_of_visits_by_lhs = models.PositiveIntegerField(verbose_name="No of visits by LHS", default=0)
    no_of_visits_by_dco_np = models.PositiveIntegerField(verbose_name="No of Visit by DCO (NP)", default=0)
    no_of_visits_by_adc_np = models.PositiveIntegerField(verbose_name="No of Visit by ADC (NP)", default=0)
    no_of_visits_by_fpo = models.PositiveIntegerField(verbose_name="No of Visit by FPO", default=0)
    no_of_visits_by_ppiu = models.PositiveIntegerField(verbose_name="No # of Visit by PPIU", default=0)

    def __str__(self):
        return "supervision"
# Create your models here.
