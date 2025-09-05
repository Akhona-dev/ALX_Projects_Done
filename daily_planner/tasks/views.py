from rest_framework import generics 
from .models import Tasks
from .serializers import TasksSerializer, UserRegistrationSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication

#----------------------------------------
#user reg
#----------------------------------------

class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]

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
    authentication_classes = [TokenAuthentication]

#--------------------------------------------------
#third view
#--------------------------------------------------

class TasksRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    authentication_classes = [TokenAuthentication]

#---------------------------------------------------
#fourth view
#---------------------------------------------------

class TasksDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    authentication_classes = [TokenAuthentication]

#---------------------------------------------------
#fith view
#---------------------------------------------------

class TaskUpdateAPIView(generics.UpdateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]