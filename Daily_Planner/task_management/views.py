from rest_framework import generics , serializers
from .models import Tasks
from . import serializers

#----------------------------------------
#first view
#----------------------------------------

class TasksListAPIView(generics.ListAPIView):

    """this line of code gets all the instances/objects/rows from the Tasks table/model"""
    queryset = Tasks.objects.all()

    """this lie of code brings the serializer class that will be responsible for converting 
       the data queried
    """
    serializer_class = serializers.TasksSerializer

#-----------------------------------------------
#second view
#-----------------------------------------------

class TasksCreateAPIView(generics.CreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = serializers.TasksSerializer

#--------------------------------------------------
#third view
#--------------------------------------------------

class TasksRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Tasks.objects.all()
    serializer_class = serializers.TasksSerializer

#---------------------------------------------------
#fourth view
#---------------------------------------------------

class TasksDeleteAPIView(generics.DestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = serializers.TasksSerializer