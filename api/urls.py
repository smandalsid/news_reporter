from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('api/google/', views.google_list),
    path('api/google/<int:pk>/', views.google_detail),
    path('api/apple/', views.apple_list),
    path('api/apple/<int:pk>/', views.apple_detail),
    path('api/meta/', views.meta_list),
    path('api/meta/<int:pk>/', views.meta_detail),
    path('api/microsoft/', views.microsoft_list),
    path('api/microsoft/<int:pk>/', views.microsoft_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
