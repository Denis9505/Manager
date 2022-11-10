from rest_framework import serializers

from .models import Transaction, UserProfile, Category


class UserSerializer(serializers.ModelSerializer):

    user=serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = UserProfile
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('user', 'category', 'count', 'time', 'organization')
