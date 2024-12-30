from django.urls import path
from . import views

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('send/<int:receiver_id>/', views.send_message, name='send_message'),
    path('view/<int:message_id>/', views.view_message, name='view_message'),
]
