from rest_framework import generics
from .models import User
from apps.transferhistory.models import HistoryTransfer
from .serializers import TransferSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class TransferDetailAPIView(generics.ListAPIView):
    queryset = HistoryTransfer.objects.all()
    serializer_class = TransferSerializer

class CreateTransferView(generics.CreateAPIView):
    serializer_class = TransferSerializer
    def post(self, request):
        transfer_user = request.data.get('from_user')
        receiver = request.data.get('to_user')
        amount = request.data.get('amount')
        from_user = User.objects.get(id=transfer_user)
        to_user = User.objects.get(id=receiver)
        from_user.balance = float(from_user.balance) - float(amount)
        receiver = float(to_user.balance) + float(amount)
        from_user.save()
        to_user.save()
        transfer = HistoryTransfer.objects.create(from_user=from_user, to_user=to_user, amount=amount)
        serializer = TransferSerializer(transfer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
