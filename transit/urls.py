from django.conf.urls import patterns, include, url

from django.contrib import admin

from rest_framework.routers import DefaultRouter

from api import views as ap
from api.driver import views as dr
from api.passenger import views as ps
from api.route import views as rs

admin.autodiscover()

router = DefaultRouter()

router.register(r'users', ap.UserViewSet)
router.register(r'drivers', dr.DriverViewSet)
router.register(r'passengers', ps.PassengerViewSet)
router.register(r'stops', rs.StopViewSet)
router.register(r'routes', rs.RouteViewSet)
router.register(r'routes', rs.AgencyViewSet)
router.register(r'services', rs.ServiceViewSet)
router.register(r'service_dates', rs.ServiceDateViewSet)
router.register(r'trip', rs.TripViewSet)


urlpatterns = patterns(
    '',
    url(r'^api/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-basic-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'),
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^docs/', include('rest_framework_swagger.urls')),
)
