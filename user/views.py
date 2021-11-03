from django.shortcuts import render
from rest_framework import mixins, viewsets
from . import serializers


class SignupViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.SignupSerializer
