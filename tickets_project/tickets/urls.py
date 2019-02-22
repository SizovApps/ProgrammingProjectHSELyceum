from django.contrib import admin
from django.urls import path
from .views import TicketsListView, TicketDetailView, TicketDeleteView, TicketUpdateView, TicketCreateView


urlpatterns = [
    path('<int:pk>/edit/ ', TicketUpdateView.as_view(), name='ticket_edit'),
    path('<int:pk>/', TicketDetailView.as_view(), name='ticket_detail'),
    path('<int:pk>/delete/', TicketDeleteView.as_view(), name='ticket_delete'),
    path('new/', TicketCreateView.as_view(), name='ticket_new'),
    path('', TicketsListView.as_view(), name='tickets_list'),
]
