from django.urls import path
from . import views
urlpatterns = [
    path('',views.home ),
    path('testing/',views.testing),
    path('testing2/', views.get_child),

    path('get_districts/',views.get_districts),
    path('get_tehsils/', views.get_tehsils, name='get-tehsils'),
    path('get_ucs/', views.get_ucs, name='get-ucs'),
    path('get_population/', views.get_population, name='get_population'),
    path('get_child/', views.get_child, name='get_child'),

    # path('division/', views.DivisionViewSet.as_view()),

    # Add other URLs as needed
]