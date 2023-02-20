from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView

from weddingmanager.orders.models import Order
from weddingmanager.theme.models import DecorItem, Item


class ThemeOrderView(DetailView):
    model = Order
    context_object_name = "order"
    template_name = "theme/theme_detail_view.html"

    def get_object(self):
        username = self.kwargs.get("username")
        user = get_user_model().objects.get(username=username)
        return Order.objects.get(user=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["items"] = Item.objects.all()
        return context


class DecorItemFile(DetailView):
    model = DecorItem
    template_name = "theme/files_details.html"


class SelectDecorItems(View):
    num = 1

    def select_decor_items(self, request):
        order = Order.objects.get(user=request.user)
        while Item.objects.all().count() != order.chosen_decor_items.count():
            item = Item.objects.get(id=self.num)
            decor_items = DecorItem.objects.filter(item=item)
            for decor_item_iteration in decor_items:
                if decor_item_iteration in order.chosen_decor_items.all():
                    break
            else:
                context = {"decor_items": decor_items, "order": order}
                return render(request, "theme/order_decor_selection.html", context)
            self.num += 1
        return render(request, "theme/decor_success.html", {"order": order})


class DecorItemSelectionView(SelectDecorItems):
    def get(self, request):
        return self.select_decor_items(request)

    def post(self, request):
        order = Order.objects.get(user=request.user)
        for key in request.POST:
            if key.startswith("decor_item"):
                decor_item_id = int(key.split("decor_item")[-1])
                decor_item = DecorItem.objects.get(id=decor_item_id)
                order.chosen_decor_items.add(decor_item)
                order.save()
                break
        return self.select_decor_items(request)


class DecorItemDeleteView(SelectDecorItems):
    def post(self, request):
        order = Order.objects.get(user=request.user)
        for key in request.POST:
            if key.startswith("decor_item"):
                decor_item_id = int(key.split("decor_item")[-1])
                order.chosen_decor_items.remove(decor_item_id)
                break
        return self.select_decor_items(request)
