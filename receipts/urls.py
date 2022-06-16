from django.urls import path
from receipts.models import Receipt

from receipts.views import ReceiptListView, ReceiptCreateView


urlpatterns = [
    path("", ReceiptListView.as_view(), name="home"),
    path("create/", ReceiptCreateView.as_view(), name='create_receipt'),
]
