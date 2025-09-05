from django.urls import path
from . import views
from .views import UserRegistrationAPIView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [

    path('api/register/', UserRegistrationAPIView.as_view(), name='api_register'),
    path('api/token-auth/', obtain_auth_token, name='api_token_auth'),

    path('Tasks/list/',views.TasksListAPIView.as_view(), name = 'list-tasks'),
    path('Tasks/create/',views.TasksCreateAPIView.as_view(), name = 'create-tasks'),
    path('Tasks/retrieve/<int:pk>/',views.TasksRetrieveAPIView.as_view(), name = 'retrieve-tasks'),
    path('Tasks/delete/<int:pk>/',views.TasksDeleteAPIView.as_view(), name = 'delete-tasks'),
    path('Tasks/update/<int:pk>/',views.TaskUpdateAPIView.as_view(), name='task-update')
]