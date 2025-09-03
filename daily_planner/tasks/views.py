from rest_framework import generics 
from .models import Tasks
from .serializers import TasksSerializer, UserRegistrationSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User

#----------------------------------------
#user reg
#----------------------------------------

class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

#----------------------------------------
#first view
#----------------------------------------


class TasksListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    """this line of code brings the serializer class that will be responsible for converting 
       the data queried
    """

    serializer_class = TasksSerializer

    """this method overrides the get_queryset method of this class and brings back tasks of only
        the currently logged in user
    """
    def get_queryset(self):
        return Tasks.objects.filter(author=self.request.user)



#-----------------------------------------------
#second view
#-----------------------------------------------

class TasksCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer

#--------------------------------------------------
#third view
#--------------------------------------------------

class TasksRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer

#---------------------------------------------------
#fourth view
#---------------------------------------------------

class TasksDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer