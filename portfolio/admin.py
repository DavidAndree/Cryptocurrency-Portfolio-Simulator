# David Alvarado
# CIS 218 
# 12/11/2024

from adminlte2_pdq.admin_menu import AdminMenu
from django.contrib import admin
from .models import Portfolio, Holding

# Register Alert model and change ALTE icons

admin.site.register(Portfolio)
AdminMenu.set_model_icon("Portfolio", "fa fa-archive")

AdminMenu.set_app_icon ("Portfolio", "fa fa-certificate")

admin.site.register(Holding)
AdminMenu.set_model_icon("Holding", "fa fa-archive")

AdminMenu.set_app_icon ("Holding", "fa fa-certificate")

# Set icons for built in user Auth
AdminMenu.set_model_icon("Group", "fa fa-users")
AdminMenu.set_model_icon("User", "fa fa-user")
AdminMenu.set_app_icon("Authentication and Authorization", "fa fa-user-o")