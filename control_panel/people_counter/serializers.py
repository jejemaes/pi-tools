from rest_framework.serializers import ModelSerializer
from rest_framework import fields

from .models import CounterItem


class CounterItemSerializer(ModelSerializer):

    count = fields.IntegerField(required=True)

    class Meta:
        model = CounterItem
        fields = ['id', 'count']
