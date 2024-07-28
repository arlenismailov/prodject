from rest_framework import serializers
from .models import *


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'phone_number', 'address', 'status')


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    salesman = serializers.StringRelatedField(source='salesman.username')
    provider = serializers.StringRelatedField(source='provider.username')
    user = serializers.StringRelatedField(source='user.username')
    status = serializers.ChoiceField(choices=Order.STATUS_CHOICES)
    announcement = serializers.StringRelatedField(source='announcement.title')

    class Meta:
        model = Order
        fields = ('id', 'salesman', 'provider', 'user', 'status', 'announcement')


class OrderCreateSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=Order.STATUS_CHOICES)

    class Meta:
        model = Order
        fields = ('id', 'salesman', 'provider', 'user', 'status', 'announcement')
