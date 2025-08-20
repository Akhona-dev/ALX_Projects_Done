from django.urls import path
from . import views

urlpatterns = [
    path('Tasks/list/',views.TasksListAPIView.as_view(), name = 'list-tasks'),
    path('Tasks/create/<int:pk>/',views.TasksCreateAPIView.as_view(), name = 'create-tasks'),
    path('Tasks/retrieve/<int:pk>/',views.TasksRetrieveAPIView.as_view(), name = 'retrieve-tasks'),
    path('Tasks/delete/<int:pk>/',views.TasksDeleteAPIView.as_view(), name = 'delete-tasks'),
]