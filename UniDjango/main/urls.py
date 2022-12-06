from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('search/certificate/<int:pk>/', views.CertificatesDetailView.as_view(), name='certificate_detail'),
    path('certificate/', views.certificate, name='certificate'),
    path('certificate/create', views.certificate_create, name='certificate_create'),
    path('search/', views.certificate_search, name='certificate_search'),
    path('contacts/', views.contact, name='contacts'),
    path('contacts/create', views.create, name='contact_create')
]