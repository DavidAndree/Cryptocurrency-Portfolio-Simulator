# David Alvarado
# CIS 218 
# 12/11/2024

from django.urls import path
from .views import AlertListView, AlertCreateView, AlertDeleteView, AlertUpdateView

urlpatterns = [
    path('list/', AlertListView.as_view(), name='list_alerts'),
    path('create/', AlertCreateView.as_view(), name='create_alert'),
    path('delete/<int:pk>/', AlertDeleteView.as_view(), name='delete_alert'),
    path('edit/<int:pk>/', AlertUpdateView.as_view(), name='edit_alert'),
]
