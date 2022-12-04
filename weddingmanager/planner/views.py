from django.views.generic import CreateView, DetailView
from django.views.generic.list import ListView

from weddingmanager.planner.forms import OrderForm
from weddingmanager.planner.models import Order, Venue

# Create your views here.


class VenueHomeView(ListView):
    model = Venue


class VenueDetailView(
    DetailView
):  # When the venue is chosen we inject the data of that venue
    model = Venue
    context_object_name = "venue"
    # slug_url_kwarg = 'slug'
    template_name = "planner/venue_services_partial.html"


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm

    def get_template_names(self, *args, **kwargs):
        if self.request.htmx:
            # TODO: in order form partial descopera if many to many is added
            return "planner/order_form_partial.html"
        else:
            return "planner/order_page.html"


# def services(request, pk):
#     pass
#     venue_chosen = get_object_or_404(Order, pk=pk)
#     venue_chosen.services.add(request.)
#     return

# def venue_chosen(request):
#     # venue = request.GET.get('venue')
#     venue = Venue.objects.get(pk=request.POST.get('venue'))
#     services = venue.services.all()
#     context = {'services': services}
#     return "planner/order_form_partial.html"

# def post(self, request, *args, **kwargs):
#     response = HttpResponse(status=204)
#     # context = super().post(request, *args, **kwargs)
#     # venue_chosen = self.get_context_data().get('venue_chosen')
#     # Services.objects.add(self.request.POST.get('service'), )
#     return trigger_client_event(response, "orderChanged", params={})
