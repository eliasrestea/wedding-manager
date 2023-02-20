from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["date"]


# def __init__(self, *args, **kwargs):
#     super().__init__(*args, **kwargs)
#     venues = Venue.objects.all()
#     self.helper = FormHelper()
#     self.helper.attrs = {
#         "hx_get": reverse("orders:detail", kwargs={"slug": self.instance.venue}),
#         "hx_target": "#services",
#     }
