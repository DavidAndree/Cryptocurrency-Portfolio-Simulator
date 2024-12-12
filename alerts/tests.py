# David Alvarado
# CIS 218 
# 12/11/2024

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Alert
from django.urls import reverse


class AlertTests(TestCase):
    """ Tests for Alerts App """
    
    def setUp(self):
        """ Create a user and log in """
        
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')


    def test_create_alert(self):
        """ Test creating an alert """
       
        # Create the alert 
        url = reverse('create_alert')
        response = self.client.post(url, {'coin': 'bitcoin', 'price_threshold': 50000, 'direction': 'UP'})

        # Check isf the alert has been created
        alert = Alert.objects.get(coin='bitcoin')
        self.assertEqual(alert.price_threshold, 50000)
        self.assertEqual(alert.direction, 'UP')
        self.assertEqual(response.status_code, 302) 


    def test_edit_alert(self):
        """ Test editing an alert """
        
        alert = Alert.objects.create(user=self.user, coin='bitcoin', price_threshold=50000, direction='UP')

        # Edit the alert
        url = reverse('edit_alert', args=[alert.id])
        response = self.client.post(url, {'coin': 'ethereum', 'price_threshold': 4000, 'direction': 'DOWN'})

        # Check if the alert has been updated
        alert.refresh_from_db()
        self.assertEqual(alert.coin, 'ethereum')
        self.assertEqual(alert.price_threshold, 4000)
        self.assertEqual(alert.direction, 'DOWN')
        self.assertEqual(response.status_code, 302)  


    def test_delete_alert(self):
        """ Test deleting an alert """ 
        
        alert = Alert.objects.create(user=self.user, coin='bitcoin', price_threshold=50000, direction='UP')

        # Delete the alert
        url = reverse('delete_alert', args=[alert.id])
        response = self.client.post(url)

        # Check if the alert is deleted
        with self.assertRaises(Alert.DoesNotExist):
            Alert.objects.get(id=alert.id)
        self.assertEqual(response.status_code, 302) 