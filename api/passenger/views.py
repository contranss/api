__author__ = 'theofilis'

from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets, status
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from .serializers import PassengerInfoSerializer
from .models import Passenger


class PassengerViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser, )
    queryset = Passenger.objects.all()
    serializer_class = PassengerInfoSerializer

    @detail_route(methods=['get', 'post', 'delete'])
    def status(self, request, pk=None):
        return Response("", status=status.HTTP_501_NOT_IMPLEMENTED)

    @detail_route(methods=['get', 'post', 'delete'])
    def favourites(self, request, pk=None):
        return Response("", status=status.HTTP_501_NOT_IMPLEMENTED)
