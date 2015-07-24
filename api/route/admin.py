__author__ = 'theofilis'

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django.contrib import admin

from models import Route, Stop, Agency, Service, Trip, TripStop, ServiceDate


class AgencyResource(resources.ModelResource):
    class Meta:
        model = Agency
        fields = ('id', 'name', 'url', 'timezone', 'lang', 'phone')


class TripResource(resources.ModelResource):
    class Meta:
        model = Trip
        fields = ('route', 'service', 'id', 'head_sign', 'direction', 'block', 'shape')


class RouteResource(resources.ModelResource):
    class Meta:
        model = Route


class ServiceResource(resources.ModelResource):
    class Meta:
        model = Service


class ServiceDateResource(resources.ModelResource):
    class Meta:
        model = ServiceDate


class StopResource(resources.ModelResource):
    class Meta:
        model = Stop
        fields = ('id', 'code', 'name', 'desc', 'lat', 'lon', 'location_type')


cid = 0


class TripStopResource(resources.ModelResource):
    class Meta:
        model = TripStop
        fields = ('trip', 'stop', 'stop_sequence', 'pickup_type', 'drop_off_type')

@admin.register(Service)
class ServiceAdmin(ImportExportModelAdmin):
    resource_class = ServiceResource


@admin.register(TripStop)
class TripStopAdmin(ImportExportModelAdmin):
    resource_class = TripStopResource


@admin.register(ServiceDate)
class ServiceDateAdmin(ImportExportModelAdmin):
    resource_class = ServiceDateResource


@admin.register(Trip)
class TripAdmin(ImportExportModelAdmin):
    resource_class = TripResource


@admin.register(Agency)
class AgencyAdmin(ImportExportModelAdmin):
    resource_class = AgencyResource


@admin.register(Stop)
class RouteAdmin(ImportExportModelAdmin):
    resource_class = StopResource


@admin.register(Route)
class RouteAdmin(ImportExportModelAdmin):
    resource_class = RouteResource

