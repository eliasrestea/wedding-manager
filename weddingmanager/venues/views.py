from django.views.generic import CreateView, DetailView
from django.views.generic.edit import FormMixin

from weddingmanager.orders.forms import OrderForm
from weddingmanager.venues.forms import VenueForm
from weddingmanager.venues.models import Service, Venue


# Create your views here.
class ServiceFile(DetailView):
    model = Service
    slug_url_kwarg = "slug"
    template_name = "venues/files_details.html"


class VenueDetailView(DetailView):
    model = Venue
    context_object_name = "venue"
    slug_url_kwarg = "slug"
    template_name = "venues/venue_details_modal.html"


class VenueServicesView(FormMixin, DetailView):
    model = Venue
    form_class = OrderForm
    context_object_name = "venue"
    slug_url_kwarg = "slug"
    template_name = "venues/venue_services_partial.html"


class VenueCreate(CreateView):
    model = Venue
    form_class = VenueForm
    template_name = "venues/venue_create.html"

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist("file_field")
        if form.is_valid():
            # Create a new object for the model
            obj = Venue()
            # Set the service_image field of the object to the list of uploaded files
            obj.service_image = files
            # Save the object to the database
            obj.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
