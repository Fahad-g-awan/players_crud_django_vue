from django.contrib import admin
from django.urls import path

from players.views import *

urlpatterns = [
    path("api/players", players, name="players"),
    
    path("admin/", admin.site.urls),
]
