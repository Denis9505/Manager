from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Transaction, UserProfile, Category
from .serializers import TransactionSerializer, UserSerializer, CategorySerializer
from .permissions import IsOwnerProfileOrReadOnly
# Create your views here.

class UserViews(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)


class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=UserProfile.objects.all()
    serializer_class=UserSerializer
    permission_classes=[IsOwnerProfileOrReadOnly, IsAuthenticated]


class CategoryListViews(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class TransactionListView(generics.ListCreateAPIView):

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
