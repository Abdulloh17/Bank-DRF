from rest_framework import generics

from .serializers import TransferSerializer
# Create your views here.

class CreateTransferView(generics.CreateAPIView):
    serializer_class = TransferSerializer