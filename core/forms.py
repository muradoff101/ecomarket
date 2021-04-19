from core.models import Couriers
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class AuthUserForm(AuthenticationForm, forms.ModelForm):

    # email = forms.EmailField(label="E-mail")
    # password = forms.CharField(widget=forms.PasswordInput, label="Пароль")

    class Meta:
        model = Couriers
        fields = ['phone', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('username')
        # self.fields['email'] = "E-mail"
        # self.fields['password'] = "Пароль"
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
