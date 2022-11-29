from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.list import ListView

from weddingmanager.planner.forms import OrderForm
from weddingmanager.planner.models import Order, Venue

# Create your views here.


class VenueHomeView(ListView):
    model = Venue


class EventCreateView(CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy("tasks:list")

    context_object_name = "venue"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["venues"] = Venue.objects.all()
        return context
