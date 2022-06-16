from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from receipts.models import Receipt
# Create your views here.


class ReceiptListView(LoginRequiredMixin, ListView):
    model = Receipt
    template_name = "receipts/receipt_list.html"
    context_object_name = "receipts"

    def get_queryset(self):
        return Receipt.objects.filter(purchaser=self.request.user)


class ReceiptCreateView(LoginRequiredMixin, CreateView):
    model = Receipt
    template_name = "receipts/create_receipt.html"
    fields = ["vendor", "total", "tax", "date", "category", "account"]
    success_url = reverse_lazy("home")


