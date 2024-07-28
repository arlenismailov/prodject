from django.urls import path
from .views import *


urlpatterns = [
    path('users/', UserViewSet.as_view({'get':'list', 'post':'create'})),
    path('users/<int:id>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    path('announcements/', AnnouncementViewSet.as_view({'get':'list', 'post':'create'})),
    path('announcements/<int:id>/', AnnouncementViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    path('orders/', OrderViewSet.as_view({'get':'list'})),
    path('orders/create/', OrderCreateViewSet.as_view({'post':'create'})),
    path('orders/create/<int:id>/', OrderCreateViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
]