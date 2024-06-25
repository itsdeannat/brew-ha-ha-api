from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Drink
from .models import Snack
from .serializers import DrinkSerializer
from .serializers import SnackSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def drinks_view(request):
    '''    
    get: 
        Presents a link of drinks. Drinks are paginated to a maximum of 10 per page.
    
    post: 
        Allows new drinks to be created.
    '''
    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST'])
def snacks_view(request):
    '''
    This view presents a link of snacks and allows new snacks to be created. 
    Snacks are paginated to a maximum of 10 per page
    '''
    if request.method == 'GET':
        snacks = Snack.objects.all()
        serializer = SnackSerializer(snacks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SnackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def drink_detail_view(request, pk):
    '''
    Retrieve a drink by its ID.
    '''
    drink = get_object_or_404(Drink, pk=pk)
    serializer = DrinkSerializer(drink)
    return Response(serializer.data)

@api_view(['GET'])
def snack_detail_view(request, pk):
    '''
    Retrieve a snack by its ID.
    '''
    snack = get_object_or_404(Snack, pk=pk)
    serializer = SnackSerializer(snack)
    return Response(serializer.data)