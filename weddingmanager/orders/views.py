from django.urls import reverse_lazy
from django.views.generic import CreateView

from weddingmanager.orders.forms import OrderForm
from weddingmanager.orders.models import Order
from weddingmanager.venues.models import Venue

# Create your views here.


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = "orders/order_page.html"
    success_url = reverse_lazy("orders:success")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["venues"] = Venue.objects.all()
        return context

    def form_valid(self, form):
        if self.request.htmx:
            form.instance.venue = Venue.objects.get(id=self.request.POST.get("id"))
            self.object = form.save()
            return super().form_valid(form)
