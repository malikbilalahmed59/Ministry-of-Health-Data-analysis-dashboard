from django.urls import path
from . import views
from .views import MotherHealthCreateView, MotherHealthDeleteView

urlpatterns = [
    path('',views.home, name='home'),
    # path('home/',views.home,name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.LoginPage,name='login'),
    path('signup/', views.SignupPage, name='signup'),
    path('logout/', views.LogoutPage, name='logout'),
    path('testing/',views.testing),
    path('testing2/', views.get_child),
    path('mother_health/add/', MotherHealthCreateView.as_view(), name='mother_health_add'),
    path('mother_health/<int:pk>/delete/', MotherHealthDeleteView.as_view(), name='mother_health_delete'),
    path('get_districts/',views.get_districts),
    path('get_tehsils/', views.get_tehsils, name='get-tehsils'),
    path('get_ucs/', views.get_ucs, name='get-ucs'),
    path('get_population/', views.get_population, name='get_population'),
    path('get_newborns_immunized_started_breastfeeding/', views.get_child, name='get_child'),
    path('get_child/', views.get_child, name='get_child'),
    path('customization/', views.Customization, name='Customization'),
    path('get_fields/', views.get_fields, name='GetFields'),
    path('get_chart_data/', views.get_chart_data, name='GetChartData'),
    path('birth_deaths/', views.child_health, name='BirthDeath'),
    path('birth_deaths_view/', views.child_health_view, name='BirthDeathView'),
    path('family_planning/', views.mother_health, name='FamilyPlanning'),
    path('family_planning_view/', views.mother_health_view, name='FamilyPlanningview'),

    # path('division/', views.DivisionViewSet.as_view()),

    # Add other URLs as needed
]