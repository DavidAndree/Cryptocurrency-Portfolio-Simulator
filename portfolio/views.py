# David Alvarado
# CIS 218 
# 12/11/2024

from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Portfolio, Holding
from management.utils import fetch_batch_crypto_prices, COIN_ID_MAP


class PortfolioView(LoginRequiredMixin, TemplateView):
    """ View for Portfolio Model """
    
    model = Portfolio
    template_name = 'portfolio.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        portfolio, created = Portfolio.objects.get_or_create(user=user)
        holdings = portfolio.holdings.all()

        live_prices = fetch_batch_crypto_prices()
        total_value = 0
        holding_details = []
        for holding in holdings:
            coin_value = holding.get_value(live_prices)
            total_value += coin_value
            holding_details.append({
                'id': holding.id,  # The ID for the delete functionality
                'coin': holding.coin,
                'quantity': holding.quantity,
                'price': live_prices.get(holding.coin.lower(), "N/A"),
                'value': coin_value,
            })

        context['portfolio'] = portfolio
        context['holdings'] = holding_details
        context['total_value'] = total_value
        return context


class AddHoldingView(LoginRequiredMixin, CreateView):
    """ View to add a Holding """
    
    model = Holding
    template_name = 'add_holding.html'
    fields = ['coin', 'quantity']
    success_url = reverse_lazy('portfolio')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['coin_choices'] = COIN_ID_MAP  # Passes coin choices to the template
        return context

    def form_valid(self, form):
        # created the users portfolio
        portfolio, created = Portfolio.objects.get_or_create(user=self.request.user)
        form.instance.portfolio = portfolio
        return super().form_valid(form)

class HoldingUpdateView(LoginRequiredMixin, UpdateView):
    """ View for Updating a Holding """
    
    model = Holding
    fields = ['coin', 'quantity'] 
    template_name = 'edit_holding.html'
    success_url = reverse_lazy('portfolio')

    def get_queryset(self):
        user = self.request.user
        portfolio = Portfolio.objects.get(user=user)
        return self.model.objects.filter(portfolio=portfolio)

class HoldingDeleteView(LoginRequiredMixin, DeleteView):
    """ View to delete a Holding """
    
    model = Holding
    template_name = 'delete_holding.html'
    success_url = reverse_lazy('portfolio')

    def get_queryset(self):
        user = self.request.user
        portfolio = get_object_or_404(Portfolio, user=user)
        return self.model.objects.filter(portfolio=portfolio)