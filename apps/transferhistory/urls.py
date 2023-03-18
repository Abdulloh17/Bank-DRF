from django.urls import path

from .views import CreateTransferView


urlpatterns = [
    path('transfer/create/', CreateTransferView.as_view(), name='create_transfer'),
]
