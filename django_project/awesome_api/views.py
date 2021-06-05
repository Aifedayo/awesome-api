from django.shortcuts import render
from rest_framework import viewsets
from awesome_api.serializers import PersonSerializer, SpeciesSerializers
from awesome_api.models import Person, Species


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer