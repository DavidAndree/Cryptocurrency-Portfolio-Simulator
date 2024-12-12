# David Alvarado
# CIS 218 
# 12/11/2024

from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Alert
from management.utils import fetch_batch_crypto_prices

class AlertListView(LoginRequiredMixin, ListView):
    """ ListView for Alerts """
    
    model = Alert
    template_name = 'list_alerts.html'
    context_object_name = 'alerts'

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        live_prices = fetch_batch_crypto_prices()  # Fetches all the  prices in one call
        for alert in queryset:
            alert.live_price = live_prices.get(alert.coin, "N/A")
        return queryset


class AlertCreateView(LoginRequiredMixin, CreateView):
    """ CreateView for a Alert """
    
    model = Alert
    template_name = 'create_alert.html'
    fields = ['coin', 'price_threshold', 'direction']
    success_url = reverse_lazy('list_alerts')

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)
    
    
class AlertUpdateView(LoginRequiredMixin, UpdateView):
    """ UpdateView for Alerts """
    
    model = Alert
    fields = ['coin', 'price_threshold', 'direction']  
    template_name = 'edit_alert.html'
    success_url = reverse_lazy('list_alerts')

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
    
    
class AlertDeleteView(LoginRequiredMixin, DeleteView):
    """ DeleteView for a specific Alert """
    
    model = Alert
    template_name = 'delete_alert.html'
    success_url = reverse_lazy('list_alerts')

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)