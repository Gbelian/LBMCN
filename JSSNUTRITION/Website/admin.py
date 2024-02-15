from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Publicite, Evenement, Team, Inscription, Contact, Newsletters

class CustomAdminSite(AdminSite):
    site_header = 'Laboratoire'
    site_title = 'Admin'
    index_title = 'Tableau de bord'

custom_admin_site = CustomAdminSite(name='customadmin')

# Enregistrez vos modèles dans la page d'administration personnalisée
custom_admin_site.register(Evenement)
custom_admin_site.register(Contact)
custom_admin_site.register(Inscription)
custom_admin_site.register(Publicite)
custom_admin_site.register(Team)
custom_admin_site.register(Newsletters)
