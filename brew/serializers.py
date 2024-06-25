from rest_framework import serializers
from .models import Drink
from .models import Snack

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model=Drink
        fields=['id', 'type', 'temperature', 'caffeine_amount', 'price']
    
class SnackSerializer(serializers.ModelSerializer):
    class Meta:
        model=Snack
        fields=['id', 'type', 'product_name', 'price']
        
