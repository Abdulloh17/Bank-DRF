from django.urls import path

from .views import CreateTransferView, TransferDetailAPIView


urlpatterns = [
    path('transfer/create/', CreateTransferView.as_view(), name='create_transfer'),
    path('transfers/', TransferDetailAPIView.as_view(), name='transfer_detail'),
]
