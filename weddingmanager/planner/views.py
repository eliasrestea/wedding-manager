from django.views.generic import CreateView, DetailView

from weddingmanager.planner.forms import OrderForm
from weddingmanager.planner.models import Order, Venue

# Create your views here.


class VenueDetailView(DetailView):
    model = Venue
    context_object_name = "venue"
    slug_url_kwarg = "slug"
    template_name = "planner/venue_details_partial.html"


class VenueServicesView(DetailView):
    model = Venue
    context_object_name = "venue"
    slug_url_kwarg = "slug"
    template_name = "planner/venue_services_partial.html"


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = "planner/order_page.html"
    success_url = "planner/order_success.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["venues"] = Venue.objects.all()
        return context

    def form_valid(self, form):
        if self.request.htmx:
            form.instance.venue = Venue.objects.get(id=self.request.POST.get("id"))
            self.object = form.save()
            return super().form_valid(form)


# if self.request.POST.get("add") in Service.objects.all():
#     self.object.chosen_services.add("service")
# return trigger_client_event(response, "orderChanged", params={})
# self.instance.chosen_services.remove("service")
# return trigger_client_event(response, "orderChanged", params={})
# else:
