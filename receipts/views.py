from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from receipts.models import Receipt, Account, ExpenseCategory
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

    def form_valid(self, form):
        form.instance.purchaser = self.request.user
        return super().form_valid(form)


class ExpenseCategoryListView(LoginRequiredMixin, ListView):
    model = ExpenseCategory
    template_name = "receipts/expense_list.html"
    context_object_name = "categories"

    def get_queryset(self):
        return ExpenseCategory.objects.filter(owner=self.request.user)


class AccountListView(LoginRequiredMixin, ListView):
    model = Account
    template_name = "receipts/account_list.html"
    context_object_name = "accounts"

    def get_queryset(self):
        return Account.objects.filter(owner=self.request.user)


class ExpenseCategoryCreateView(LoginRequiredMixin, CreateView):
    model = ExpenseCategory
    template_name = "receipts/create_expense_category.html"
    fields = ["name"]

    def form_valid(self, form):
        item = form.save(commit=False)
        item.owner = self.request.user
        item.save()
        return redirect("category_list")


class AccountCreateView(LoginRequiredMixin, CreateView):
    model = Account
    template_name = "receipts/create_account.html"
    fields = ["name", "number"]

    def form_valid(self, form):
        item = form.save(commit=False)
        item.owner = self.request.user
        item.save()
        return redirect("account_list")