from django.contrib.auth import get_user_model
from django.forms import forms
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView

from weddingmanager.orders.models import Order
from weddingmanager.venues.models import Service, Venue

# Create your views here.


class OrderCreateView(FormView):
    template_name = "orders/order_page.html"
    success_url = reverse_lazy("orders:success")
    form_class = forms.Form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["venues"] = Venue.objects.all()
        return context

    def form_valid(self, form):
        if self.request.htmx:
            # Get the IDs of the chosen services
            service_ids = self.request.POST.getlist("services")
            # Get the chosen venue
            venue_id = self.request.POST.get("id")
            venue = Venue.objects.get(id=venue_id)
            total_price = venue.venue_price
            # Create a new Order object
            order = Order(venue=venue, user=self.request.user)
            order.save()

            # Add the chosen services to the Order object
            for service_id in service_ids:
                service = Service.objects.get(id=service_id)
                order.chosen_services.add(service)
                total_price += service.service_price
            # Add the price of the order
            order.total_price = total_price
            order.save()
        return super().form_valid(form)


class OrderDetailView(DetailView):
    model = Order
    context_object_name = "order"
    template_name = "orders/order_detail_view.html"

    def get_object(self):
        username = self.kwargs.get("username")
        user = get_user_model().objects.get(username=username)
        return Order.objects.get(user=user)
