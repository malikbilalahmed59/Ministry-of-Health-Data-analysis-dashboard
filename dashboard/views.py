from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from dashboard.models import District, Division, UC, Tehsil, Facility, ChildHealth
from dashboard.serializer import DivisionSerializer


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
    print(total_12_23_months_old_children)

    return render(request, 'index.html',{'divisions': divisions})

def testing(request):
    divisions = Division.objects.all()

    return render(request, 'testing.html',{'divisions': divisions})

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




# def get_fac(request):


# Create your views here.
