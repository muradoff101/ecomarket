from django.db.models import query
from django.shortcuts import render
from rest_framework import generics
from core.serializers import *
from rest_framework.permissions import IsAuthenticated
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework import status
from core.forms import AuthUserForm
from django.contrib.auth import authenticate, login

# Create your views here.


class RegisterDevices(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DeviceSerializers

    def perform_create(self, serializer):
        serializer.save(courier=self.request.user)


class RegisterLocations(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LocationSerializer


class BaseListView(ListView):
    paginate_by = 20

    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('/login/')
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['couriers_count'] = Couriers.objects.count()
        context['companies_count'] = Companies.objects.count()
        context['devices_count'] = Devices.objects.count()
        return context


class BaseDetailView(DetailView):
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('/login/')
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['couriers_count'] = Couriers.objects.count()
        context['companies_count'] = Companies.objects.count()
        context['devices_count'] = Devices.objects.count()
        return context


class MainPage(BaseListView):
    template_name = "index.html"
    context_object_name = "info"
    queryset = Companies.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['locations'] = Locations.objects.all()
        return context


class CouriersListPage(BaseListView):
    template_name = "couriers.html"
    context_object_name = "couriers"
    queryset = Couriers.objects.all()


class CompaniesListPage(BaseListView):
    template_name = "companies.html"
    context_object_name = "companies"
    queryset = Companies.objects.all()


class DevicesListPage(BaseListView):
    template_name = "devices.html"
    context_object_name = "devices"
    queryset = Devices.objects.all()


class LocationsListPage(BaseListView):
    template_name = "locations.html"
    context_object_name = "locations"
    queryset = Locations.objects.all()


class LoginPage(LoginView):
    template_name = 'login.html'
    # authentication_form = AuthUserForm
    success_url = reverse_lazy('main_page_link')

    def get_success_url(self):
        return self.success_url

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(*args, **kwargs)


class LogoutPage(LogoutView):
    next_page = reverse_lazy('login_page_link')
