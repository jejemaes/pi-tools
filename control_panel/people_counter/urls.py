from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views
from . views import CounterItemsModelViewSet


# Page routes
urlpatterns = [
    path('', views.page_counter),
]

# API routes
router = SimpleRouter()
router.register(r'api/counter', CounterItemsModelViewSet, basename='counteritems')

urlpatterns += router.urls
