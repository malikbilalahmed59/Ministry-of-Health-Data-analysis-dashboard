# Generated by Django 4.2.6 on 2023-10-08 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasicInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_health_committees_formulated', models.BooleanField(default=False, verbose_name='Is Health Committees Formulated')),
                ('is_women_support_groups_formulated', models.BooleanField(default=False, verbose_name='Is Women Support Groups Formulated')),
                ('household_registered_by_lhws', models.PositiveIntegerField(default=0, verbose_name='Household Registered by LHWs')),
                ('household_using_iodine_salt', models.PositiveIntegerField(default=0, verbose_name='Household Using Iodine Salt')),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility', models.CharField(max_length=255)),
                ('area_type_id', models.PositiveIntegerField(blank=True, null=True)),
                ('population', models.PositiveIntegerField(blank=True, null=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.district')),
            ],
        ),
        migrations.CreateModel(
            name='LHW',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lhw_code', models.CharField(max_length=20, unique=True)),
                ('lhw_name', models.CharField(max_length=255)),
                ('lhw_cnic', models.CharField(max_length=15, unique=True)),
                ('lhw_father_husband_name', models.CharField(max_length=255)),
                ('catchment_population_flcf', models.PositiveIntegerField()),
                ('population_registered_by_lhws', models.PositiveIntegerField()),
                ('lhw_attached_facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.facility')),
                ('lhw_district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.district')),
            ],
        ),
        migrations.CreateModel(
            name='Tehsil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tehsil', models.CharField(max_length=255)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.district')),
            ],
        ),
        migrations.CreateModel(
            name='UC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uc', models.CharField(max_length=255)),
                ('tehsil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.tehsil')),
            ],
        ),
        migrations.CreateModel(
            name='Supervision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_visits_by_lhs', models.PositiveIntegerField(default=0, verbose_name='No of visits by LHS')),
                ('no_of_visits_by_dco_np', models.PositiveIntegerField(default=0, verbose_name='No of Visit by DCO (NP)')),
                ('no_of_visits_by_adc_np', models.PositiveIntegerField(default=0, verbose_name='No of Visit by ADC (NP)')),
                ('no_of_visits_by_fpo', models.PositiveIntegerField(default=0, verbose_name='No of Visit by FPO')),
                ('no_of_visits_by_ppiu', models.PositiveIntegerField(default=0, verbose_name='No # of Visit by PPIU')),
                ('lhw_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supervision', to='dashboard.lhw')),
            ],
        ),
        migrations.CreateModel(
            name='SocialContacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_health_committee_meetings', models.PositiveIntegerField(default=0)),
                ('no_women_support_group_meetings', models.PositiveIntegerField(default=0)),
                ('no_health_education_sessions_in_school', models.PositiveIntegerField(default=0)),
                ('lhw_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_contacts', to='dashboard.lhw')),
            ],
        ),
        migrations.CreateModel(
            name='SewerageSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pit', models.PositiveIntegerField(default=0, verbose_name='Pit')),
                ('flush_system', models.PositiveIntegerField(default=0, verbose_name='Flush System')),
                ('open_fields', models.PositiveIntegerField(default=0, verbose_name='Open Fields')),
                ('total', models.PositiveIntegerField(default=0, verbose_name='Total')),
                ('basic_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.basicinformation')),
            ],
        ),
        migrations.CreateModel(
            name='MotherHealth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_newly_registered_pregnant_women', models.PositiveIntegerField(default=0)),
                ('total_pregnant_women', models.PositiveIntegerField(default=0)),
                ('total_pregnant_women_visited', models.PositiveIntegerField(default=0)),
                ('no_pregnant_breastfeeding_women_mauc_done', models.PositiveIntegerField(default=0)),
                ('no_pregnant_breastfeeding_malnutrition_women_mauc', models.PositiveIntegerField(default=0)),
                ('no_pregnant_women_supplied_iron_tablets', models.PositiveIntegerField(default=0)),
                ('no_abortions', models.PositiveIntegerField(default=0)),
                ('total_deliveries', models.PositiveIntegerField(default=0)),
                ('no_women_delivered_provided_misoprostol', models.PositiveIntegerField(default=0)),
                ('no_women_delivered_anc_visits_by_sbas', models.PositiveIntegerField(default=0)),
                ('no_women_delivered_tt_completed_before_delivery', models.PositiveIntegerField(default=0)),
                ('no_deliveries_by_skilled_birth_attendants', models.PositiveIntegerField(default=0)),
                ('no_postnatal_cases_visited_within_24_hours', models.PositiveIntegerField(default=0)),
                ('lhw_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mother_health', to='dashboard.lhw')),
            ],
        ),
        migrations.CreateModel(
            name='lhw_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.facility')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.uc')),
            ],
        ),
        migrations.AddField(
            model_name='lhw',
            name='lhw_tehsil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.tehsil'),
        ),
        migrations.AddField(
            model_name='lhw',
            name='lhw_union_council',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.uc'),
        ),
        migrations.CreateModel(
            name='HouseholdWithDrinkingWaterSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tap', models.PositiveIntegerField(default=0, verbose_name='Tap (Public Health - Engineering)')),
                ('hand_pump', models.PositiveIntegerField(default=0, verbose_name='Hand Pump / Motor Pump')),
                ('spring', models.PositiveIntegerField(default=0, verbose_name='Spring')),
                ('well', models.PositiveIntegerField(default=0, verbose_name='Well')),
                ('other', models.PositiveIntegerField(default=0, verbose_name='Other')),
                ('total', models.PositiveIntegerField(default=0, verbose_name='Total')),
                ('basic_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.basicinformation')),
            ],
        ),
        migrations.CreateModel(
            name='FamilyPlanning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_eligible_couples', models.PositiveIntegerField(default=0)),
                ('no_new_clients_family_planning', models.PositiveIntegerField(default=0)),
                ('no_followup_cases_family_planning', models.PositiveIntegerField(default=0)),
                ('total_traditional_method_users', models.PositiveIntegerField(default=0)),
                ('total_modern_contraceptive_users', models.PositiveIntegerField(default=0)),
                ('no_condom_users', models.PositiveIntegerField(default=0)),
                ('no_oral_pills_users', models.PositiveIntegerField(default=0)),
                ('no_coc_users', models.PositiveIntegerField(default=0)),
                ('no_ecp_users', models.PositiveIntegerField(default=0)),
                ('no_injectable_contraceptive_users', models.PositiveIntegerField(default=0)),
                ('no_2_month_injection', models.PositiveIntegerField(default=0)),
                ('no_3_month_injection', models.PositiveIntegerField(default=0)),
                ('no_iucd_clients', models.PositiveIntegerField(default=0)),
                ('no_surgical_clients', models.PositiveIntegerField(default=0)),
                ('no_other_modern_contraceptive_users', models.PositiveIntegerField(default=0)),
                ('no_clients_referred', models.PositiveIntegerField(default=0)),
                ('no_clients_supplied_condoms', models.PositiveIntegerField(default=0)),
                ('no_clients_supplied_oral_pills', models.PositiveIntegerField(default=0)),
                ('no_clients_administered_injectable_contraceptives', models.PositiveIntegerField(default=0)),
                ('lhw_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='family_planning', to='dashboard.lhw')),
            ],
        ),
        migrations.AddField(
            model_name='facility',
            name='tehsil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.tehsil'),
        ),
        migrations.AddField(
            model_name='facility',
            name='uc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.uc'),
        ),
        migrations.AddField(
            model_name='district',
            name='division',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.division'),
        ),
        # migrations.CreateModel(
        #     name='ChildHealth',
        #     fields=[
        #         ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('no_newborns_weighted', models.PositiveIntegerField(default=0)),
        #         ('no_low_birth_weight_babies', models.PositiveIntegerField(default=0)),
        #         ('no_newborn_started_breast_feeding', models.PositiveIntegerField(default=0)),
        #         ('no_newborn_applied_chlorhexidine', models.PositiveIntegerField(default=0)),
        #         ('no_newborn_immunization_started', models.PositiveIntegerField(default=0)),
        #         ('no_6_months_old_children', models.PositiveIntegerField(default=0)),
        #         ('no_6_months_old_children_exclusive_breast_feeding', models.PositiveIntegerField(default=0)),
        #         ('no_6_59_months_old_children', models.PositiveIntegerField(default=0)),
        #         ('no_6_59_months_old_children_mauc_done', models.PositiveIntegerField(default=0)),
        #         ('no_6_59_months_children_malnutrition_mauc', models.PositiveIntegerField(default=0)),
        #         ('no_6_59_months_children_malnutrition_less_than_mauc', models.PositiveIntegerField(default=0)),
        #         ('no_12_23_months_old_children', models.PositiveIntegerField(default=0)),
        #         ('no_12_23_months_old_children_fully_immunized', models.PositiveIntegerField(default=0)),
        #         ('no_5_years_children', models.PositiveIntegerField(default=0)),
        #         ('no_5_years_children_micro_nutrition_sachet', models.PositiveIntegerField(default=0)),
        #         ('no_5_years_children_gm_done_recorded', models.PositiveIntegerField(default=0)),
        #         ('no_5_years_children_low_weight', models.PositiveIntegerField(default=0)),
        #         ('lhw_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_health', to='dashboard.lhw')),
        #     ],
        # ),
        migrations.CreateModel(
            name='BirthsDeaths',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_live_births', models.PositiveIntegerField(default=0)),
                ('no_still_births', models.PositiveIntegerField(default=0)),
                ('no_all_deaths', models.PositiveIntegerField(default=0)),
                ('no_neonatal_deaths', models.PositiveIntegerField(default=0)),
                ('no_infant_deaths_week', models.PositiveIntegerField(default=0)),
                ('no_infant_deaths_month', models.PositiveIntegerField(default=0)),
                ('no_children_deaths', models.PositiveIntegerField(default=0)),
                ('no_maternal_deaths', models.PositiveIntegerField(default=0)),
                ('lhw_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='birth_deaths', to='dashboard.lhw')),
            ],
        ),
        migrations.AddField(
            model_name='basicinformation',
            name='lhw_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basic_information', to='dashboard.lhw'),
        ),
    ]
