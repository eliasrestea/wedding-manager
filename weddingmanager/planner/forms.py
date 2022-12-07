from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     venues = Venue.objects.all()
    #     self.helper = FormHelper()
    #     self.helper.attrs = {
    #         "hx_get": reverse("planner:detail", kwargs={"slug": self.instance.venue}),
    #         "hx_target": "#services",
    #     }
    class Meta:
        model = Order
        fields = ["chosen_services"]

        # widgets = {"venue": forms.RadioSelect()}
