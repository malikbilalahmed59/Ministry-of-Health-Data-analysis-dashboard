from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.db.models import Count
from django.views.generic import CreateView, DeleteView
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework.viewsets import ModelViewSet
from django.db.models import Sum
from django.http import JsonResponse
from django.apps import apps

from dashboard.models import District, Division, UC, Tehsil, Facility, ChildHealth, Supervision, MotherHealth, \
    FamilyPlanning, BirthsDeaths
from dashboard.serializer import DivisionSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm, LoginForm, MotherHealthForm, BirthsDeathsForm
from django.urls import reverse_lazy
from .models import MotherHealth
from .forms import FamilyPlanningForm


def child_health(request):
    # form = MotherHealthForm.objects.all()
    if request.method == 'POST':
        form = BirthsDeathsForm(request.POST)
        if form.is_valid():
            # Process the form data if needed
            BirthsDeaths_instance = form.save(commit=False)
            BirthsDeaths_instance.save()
            return redirect('home')
        else:
            form = BirthsDeathsForm()
    else:
        form = BirthsDeathsForm()

        # Fetch related lhw_info data efficiently using select_related
    BirthsDeaths_data = BirthsDeaths.objects.select_related('lhw_code').all()
    return render(request, 'child_health.html', {'BirthsDeaths_data':BirthsDeaths_data,'form':form})


def mother_health(request):
    if request.method == 'POST':
        form = FamilyPlanningForm(request.POST)
        if form.is_valid():
            # Process the form data if needed
            family_planning_instance = form.save(commit=False)
            family_planning_instance.save()
            return redirect('home')
        else:
            form = FamilyPlanningForm()
    else:
        form = FamilyPlanningForm()

    # Fetch related lhw_info data efficiently using select_related
    family_planning_data = FamilyPlanning.objects.select_related('lhw_code').all()

    return render(request, 'mother_health.html', {'form': form, 'family_planning_data': family_planning_data})


def child_health_view(request):

    BirthsDeaths_data = BirthsDeaths.objects.select_related('lhw_code').all()
    print(BirthsDeaths_data[0].no_live_births)

    return render(request, 'child_health_view.html',{'context': BirthsDeaths_data})


def mother_health_view(request):
    family_planning_data = FamilyPlanning.objects.select_related('lhw_code').all()

    return render(request, 'mother_health_view.html',{'context': family_planning_data})


def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'signin.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')


class MotherHealthCreateView(CreateView):
    model = MotherHealth
    form_class = MotherHealthForm
    template_name = 'mother_health_form.html'  # Adjust the path to your template
    success_url = '/success/'


class MotherHealthDeleteView(DeleteView):
    model = MotherHealth
    template_name = 'mother_health_confirm_delete.html'  # Adjust the path to your template
    success_url = reverse_lazy('home.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to the home page
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})


@login_required(login_url='login')
def home(request):
    divisions = Division.objects.all()
    total_newborns_weighted = ChildHealth.objects.aggregate(Sum('no_newborns_weighted'))[
                                  'no_newborns_weighted__sum'] or 0
    age_group_counts = ChildHealth.objects.values('no_6_months_old_children', 'no_6_59_months_old_children',
                                                  'no_12_23_months_old_children', 'no_5_years_children').aggregate(
        Sum('no_6_months_old_children'),
        Sum('no_6_59_months_old_children'),
        Sum('no_12_23_months_old_children'),
        Sum('no_5_years_children')
    )
    total_12_23_months_old_children = ChildHealth.objects.aggregate(Sum('no_12_23_months_old_children'))[
                                          'no_12_23_months_old_children__sum'] or 1  # Avoid division by zero
    fully_immunized_percentage = (ChildHealth.objects.filter(
        no_12_23_months_old_children_fully_immunized__gt=0).count() / total_12_23_months_old_children) * 100

    data = MotherHealth.objects.all()

    # Example preprocessing: Convert queryset to a list of dictionaries
    chart_data = [
        {
            'label': 'Total Pregnant Women',
            'data': [entry.total_pregnant_women for entry in data]
        },
        {
            'label': 'No. Pregnant Breastfeeding Malnutrition Women',
            'data': [entry.no_pregnant_breastfeeding_malnutrition_women_mauc for entry in data]
        },
        {
            'label': 'No. Abortions',
            'data': [entry.no_abortions for entry in data]
        },
    ]
    aggregated_data = Supervision.objects.aggregate(
        total_visits_lhs=Sum('no_of_visits_by_lhs'),
        total_visits_dco_np=Sum('no_of_visits_by_dco_np'),
        total_visits_adc_np=Sum('no_of_visits_by_adc_np'),
        total_visits_fpo=Sum('no_of_visits_by_fpo'),
        total_visits_ppiu=Sum('no_of_visits_by_ppiu'),
    )

    # Pass the aggregated data to the template
    context = {
        'aggregated_data': aggregated_data,
    }
    print(context)
    family_planning_data = FamilyPlanning.objects.select_related('lhw_code').all()

    return render(request, 'home.html', {'family_planning_data':family_planning_data,'divisions': divisions, 'context': context, 'chart_data': chart_data})


def testing(request):
    divisions = Division.objects.all()

    return render(request, 'testing.html', {'divisions': divisions})


from django.http import JsonResponse


def get_districts(request):
    division_id = request.GET.get('division_id', None)
    if division_id:
        districts = District.objects.filter(division_id=division_id).values('id', 'district')
        data = {district['id']: district['district'] for district in districts}
        return JsonResponse(data)
    else:
        return JsonResponse({})


def get_tehsils(request):
    district_id = request.GET.get('district_id', None)
    if district_id:
        tehsils = Tehsil.objects.filter(district_id=district_id).values('id', 'tehsil')
        data = {tehsil['id']: tehsil['tehsil'] for tehsil in tehsils}
        return JsonResponse(data)
    else:
        return JsonResponse({})


def get_ucs(request):
    tehsil_id = request.GET.get('tehsil_id', None)
    if tehsil_id:
        ucs = UC.objects.filter(tehsil_id=tehsil_id).values('id', 'uc')
        data = {uc['id']: uc['uc'] for uc in ucs}
        return JsonResponse(data)
    else:
        return JsonResponse({})


from django.db.models import Sum


def get_population(request):
    try:
        division_id = request.GET.get('division_id')
        district_id = request.GET.get('district_id')
        tehsil_id = request.GET.get('tehsil_id')
        uc_id = request.GET.get('uc_id')

        # Convert string values to integers
        district_id = int(district_id) if district_id else None

        # Query to get population based on division and/or district
        population_query = Facility.objects.filter(
            tehsil__district__division_id=division_id
        )

        if district_id:
            population_query = population_query.filter(district_id=district_id)

        if tehsil_id:
            population_query = population_query.filter(tehsil_id=tehsil_id)
        if uc_id:
            population_query = population_query.filter(uc_id=uc_id)

        population = population_query.aggregate(total_population=Sum('population'))

        return JsonResponse({'total_population': population['total_population'] or 0})

    except ObjectDoesNotExist as e:
        return JsonResponse({'error': f'Object does not exist: {e}'}, status=404)

    except Exception as e:
        # Log the error for debugging
        print(f'Error in get_population: {e}')

        # Return an error response
        return JsonResponse({'error': 'Internal Server Error'}, status=500)


def get_child(request):
    # Example 1: Get Total Count of Newborns Weighted
    division_id = request.GET.get('division_id')
    district_id = request.GET.get('district_id')
    tehsil_id = request.GET.get('tehsil_id')
    uc_id = request.GET.get('uc_id')

    # Convert string values to integers
    division_id = int(division_id) if division_id else None
    district_id = int(district_id) if district_id else None
    tehsil_id = int(tehsil_id) if tehsil_id else None
    uc_id = int(uc_id) if uc_id else None

    # Create a filter dictionary based on the provided parameters
    filter_dict = {}

    if division_id:
        filter_dict['lhw_code__facility__tehsil__district__division_id'] = division_id

    if district_id:
        filter_dict['lhw_code__facility__tehsil__district_id'] = district_id

    if tehsil_id:
        filter_dict['lhw_code__facility__tehsil_id'] = tehsil_id

    if uc_id:
        filter_dict['lhw_code__facility__uc_id'] = uc_id

    # Query to get child health data based on the filters
    child_health_data = ChildHealth.objects.filter(**filter_dict)

    # Example: Aggregate the sum of 'no_newborns_weighted' for the filtered data
    total_newborns_weighted = child_health_data.aggregate(Sum('no_newborns_weighted'))['no_newborns_weighted__sum'] or 0

    # Example: Get Counts for Each Age Group
    age_group_counts = child_health_data.values(
        'no_6_months_old_children',
        'no_6_59_months_old_children',
        'no_12_23_months_old_children',
        'no_5_years_children'
    ).aggregate(
        Sum('no_6_months_old_children'),
        Sum('no_6_59_months_old_children'),
        Sum('no_12_23_months_old_children'),
        Sum('no_5_years_children')
    )

    # Example: Get Percentage of Fully Immunized Children among 12-23 Months Old
    total_12_23_months_old_children = child_health_data.aggregate(Sum('no_12_23_months_old_children'))[
                                          'no_12_23_months_old_children__sum'] or 1
    fully_immunized_percentage = (child_health_data.filter(
        no_12_23_months_old_children_fully_immunized__gt=0).count() / total_12_23_months_old_children) * 100
    context = {
        'total_newborns_weighted': total_newborns_weighted,
        'age_group_counts': age_group_counts,
        'fully_immunized_percentage': fully_immunized_percentage,
    }

    return JsonResponse(context)


def Customization(request):
    divisions = Division.objects.all()

    return render(request, 'customization.html', {'divisions': divisions})


def get_fields(request):
    selected_table = request.POST.get('selectedTable')

    if selected_table == 'Child Health':
        model = ChildHealth
    elif selected_table == 'Mother Health':
        model = MotherHealth
    else:
        return JsonResponse({'error': 'Invalid table selected'})

    # Get all field names excluding the primary key
    fields = [field.name for field in model._meta.get_fields() if field.name != 'id']

    context = {
        'fields': fields
    }

    return JsonResponse(context)


def get_chart_data(request):
    selected_tables = request.POST.getlist('selected_table[]')
    selected_fields = request.POST.getlist('selected_fields[]')

    chart_data = {}

    for selected_table in selected_tables:
        if selected_table == 'Child Health':
            model = ChildHealth
        elif selected_table == 'Mother Health':
            model = MotherHealth
        else:
            return JsonResponse({'error': 'Invalid table selected'})

        # Print or log the available fields for debugging
        print(f"Available fields for {selected_table}: {model._meta.get_fields()}")

        # Fetch data based on selected fields dynamically
        data = model.objects.values(*selected_fields)

        # Convert queryset to a list of dictionaries
        data_list = list(data)

        # Perform dynamic aggregations for each field
        for field in selected_fields:
            total_field = f'total_{selected_table}_{field}'
            chart_data[total_field] = data.aggregate(Sum(field)).get(field + '__sum', 0)

    return JsonResponse({'chart_data': chart_data})

# def get_fac(request):


# Create your views here.
