from rest_framework import serializers
from base.models import Item

class ItemSerializer(serializers.ModelSerializers):
    class Meta:
        model = Item
        fields = '__all__'