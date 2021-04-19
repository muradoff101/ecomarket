from django.urls import path
from core.views import *

urlpatterns = [
    path("api/v1/register-device/", RegisterDevices.as_view()),
    path("api/v1/register-location/", RegisterLocations.as_view()),
    # path("api/v1/login/", LoginUser.as_view()),
    path("", MainPage.as_view(), name="main_page_link"),
    path("couriers/", CouriersListPage.as_view(),
         name="couriers_list_page_link"),
    path("company/", CompaniesListPage.as_view(),
         name='companies_list_page_link'),
    path("devices/", DevicesListPage.as_view(), name="devices_list_page_link"),
    path("login/", LoginPage.as_view(), name="login_page_link"),
    path("logout/", LogoutPage.as_view(), name="logout_page_link"),
    path("locations/", LocationsListPage.as_view(), name="location_page_link")


]
