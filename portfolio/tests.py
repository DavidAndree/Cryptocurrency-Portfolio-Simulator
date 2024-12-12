# David Alvarado
# CIS 218 
# 12/11/2024

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Portfolio, Holding
from django.urls import reverse


class PortfolioTests(TestCase):
    """ Tests for Portfolio App """
    def setUp(self):
        """ Create a user and portfolio for testing """  
        
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

        self.portfolio = Portfolio.objects.create(user=self.user)


    def test_add_holding(self):
        """Test adding a holding to the portfolio."""
        
        url = reverse('add_holding')
        response = self.client.post(url, {'coin': 'bitcoin', 'quantity': 1.0})

        # Check if holding is added
        holding = Holding.objects.get(coin='bitcoin', portfolio=self.portfolio)
        self.assertEqual(holding.quantity, 1.0)
        self.assertEqual(response.status_code, 302)  # the redirect after successful creation


    def test_edit_holding(self):
        """ Test editing an existing holding """
        
        holding = Holding.objects.create(coin='bitcoin', quantity=1.0, portfolio=self.portfolio)

        # Edit for the holding
        url = reverse('edit_holding', args=[holding.id])
        response = self.client.post(url, {'coin': 'ethereum', 'quantity': 2.0})

        # Check if the holding has been updated
        holding.refresh_from_db()
        self.assertEqual(holding.coin, 'ethereum')
        self.assertEqual(holding.quantity, 2.0)
        self.assertEqual(response.status_code, 302)  


    def test_delete_holding(self):
        """Test deleting a holding from the portfolio """
        
        holding = Holding.objects.create(coin='bitcoin', quantity=1.0, portfolio=self.portfolio)

        # Delete the holding
        url = reverse('delete_holding', args=[holding.id])
        response = self.client.post(url)

        # Check if the holding is deleted
        with self.assertRaises(Holding.DoesNotExist):
            Holding.objects.get(id=holding.id)
        self.assertEqual(response.status_code, 302) 


    def test_total_portfolio_value(self):
        """Test if the total portfolio value is calculated correctly """
            
        holding1 = Holding.objects.create(coin='bitcoin', quantity=1.0, portfolio=self.portfolio)
        holding2 = Holding.objects.create(coin='ethereum', quantity=2.0, portfolio=self.portfolio)

        # Assume the test prices for testing
        mock_prices = {'bitcoin': 50000, 'ethereum': 3000}
        total_value = holding1.quantity * mock_prices['bitcoin'] + holding2.quantity * mock_prices['ethereum']