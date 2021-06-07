from django.urls import include, path

from rest_framework import router

from awesome_api.views import PersonViewSet, SpeciesViewSet

router = routers.DefaultRouter()