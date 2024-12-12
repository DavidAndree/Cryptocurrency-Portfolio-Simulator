# David Alvarado
# CIS 218 
# 12/11/2024

from django.urls import path
from .views import PortfolioView, AddHoldingView, HoldingDeleteView, HoldingUpdateView

urlpatterns = [
    path('', PortfolioView.as_view(), name='portfolio'),
    path('add/', AddHoldingView.as_view(), name='add_holding'),
    path('delete/<int:pk>/', HoldingDeleteView.as_view(), name='delete_holding'),
    path('edit/<int:pk>/', HoldingUpdateView.as_view(), name='edit_holding'),

]