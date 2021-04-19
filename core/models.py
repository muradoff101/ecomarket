from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.deletion import DO_NOTHING

# Create your models here.


class CouriersManager(BaseUserManager):
    def create_user(self, phone, full_name, password=None):
        if not phone:
            raise ValueError("Phone must be")
        if not full_name:
            raise ValueError("Full name must be")

        user = self.model(
            # phone=self.normalize_email(email),
            phone=phone,
            full_name=full_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, full_name, password):
        user = self.create_user(
            # email=self.normalize_email(email),
            phone=phone,
            password=password,
            full_name=full_name
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)


class Couriers(AbstractBaseUser):
    phone = models.DecimalField(
        "Phone number", max_digits=12, decimal_places=0, unique=True)
    full_name = models.CharField("Full name", max_length=255)
    pasp_number = models.CharField(
        "Passport number", max_length=255, blank=True)
    address = models.CharField("Address", max_length=255, blank=True)
    date_joined = models.DateTimeField(
        "Registered date", auto_now_add=True, null=True)
    last_login = models.DateTimeField(
        "Last login date", auto_now=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ["full_name"]

    objects = CouriersManager()

    class Meta:
        # app_label = 'clients_auth'
        # db_table = 'clients_user'
        verbose_name = "Courier"
        verbose_name_plural = "Couriers"

    def __str__(self) -> str:
        return str(self.full_name)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def authenticate(self, request, phone=None, password=None, **kwargs):
        try:
            user = Couriers.objects.get(phone=phone)
            if user.check_password(password):
                return user
        except Couriers.MultipleObjectsReturned:
            return None
        except Couriers.DoesNotExist:
            return None
        return None


class Companies(models.Model):
    name = models.CharField("Company name", max_length=255)
    created_at = models.DateField("Created at", auto_now_add=True,)
    updated_at = models.DateField("Updated at", auto_now=True)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self) -> str:
        return self.name


class Devices(models.Model):
    company = models.ForeignKey(
        Companies, verbose_name="Company", on_delete=models.CASCADE)
    device_id = models.CharField("Device ID", max_length=32)
    device_model = models.CharField("Device model", max_length=255)
    created_at = models.DateField("Created at", auto_now_add=True)
    updated_at = models.DateField("Updated at", auto_now=True)
    app = models.CharField("App name", max_length=255)
    version = models.CharField("App version", max_length=10)
    courier = models.ForeignKey(
        Couriers, verbose_name="Courier", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Device"
        verbose_name_plural = "Devices"

    def __str__(self) -> str:
        return self.device_model


class Locations(models.Model):
    latitude = models.DecimalField(
        "Latitude", max_digits=22, decimal_places=16)
    longitude = models.DecimalField(
        "Longitude", max_digits=22, decimal_places=16)
    created_at = models.DateField("Created at", auto_now_add=True)
    updated_at = models.DateField("Updated at", auto_now=True)
    company = models.ForeignKey(
        Companies, verbose_name="Company", on_delete=models.CASCADE)
    device = models.ForeignKey(
        Devices, verbose_name="Device", on_delete=models.CASCADE)
    data = models.CharField("Some data", max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"

    def __str__(self) -> str:
        return str(self.id)
