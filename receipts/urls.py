from django.urls import path
from receipts.models import Receipt

from receipts.views import ReceiptListView


urlpatterns = [
    path("", ReceiptListView.as_view(), name="home"),
]
