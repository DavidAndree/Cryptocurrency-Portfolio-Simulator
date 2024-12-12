# David Alvarado
# CIS 218 
# 12/11/2024

from adminlte2_pdq.admin_menu import AdminMenu
from django.contrib import admin
from .models import Alert

# Register Alert model and change ALTE icons

admin.site.register(Alert)
AdminMenu.set_model_icon("Alert", "fa fa-archive")

AdminMenu.set_app_icon ("Alerts", "fa fa-certificate")

# Set icons for built in user Auth
AdminMenu.set_model_icon("Group", "fa fa-users")
AdminMenu.set_model_icon("User", "fa fa-user")
AdminMenu.set_app_icon("Authentication and Authorization", "fa fa-user-o")