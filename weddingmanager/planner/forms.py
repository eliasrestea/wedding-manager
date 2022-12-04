from crispy_forms.helper import FormHelper
from django import forms
from django.urls import reverse

from .models import Order


class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.attrs = {
            # todo alpine js inlocuieste self.instace.venue cu ceva pe fiecare buton
            "hx_get": reverse("planner:detail", kwargs={"slug": self.instance.venue}),
            "hx_target": "#services",
            "hx_push_url": "true",
        }

    class Meta:
        model = Order
        fields = ["venue"]

        widgets = {"venue": forms.RadioSelect()}
