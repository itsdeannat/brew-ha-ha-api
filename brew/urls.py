from django.urls import path
from .views import drinks_view
from .views import snacks_view
from .views import drink_detail_view
from .views import snack_detail_view

urlpatterns = [
    path('drinks/', drinks_view, name='drinks_view'),
    path('snacks/', snacks_view, name='snacks_view'),
    path('drinks/<int:pk>/', drink_detail_view, name='drink-detail'),
    path('snacks/<int:pk>/', snack_detail_view, name='snack-detail')
]