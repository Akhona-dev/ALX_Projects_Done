from django.db import models
from django.contrib.auth.models import User

"""the following line of code creates a table named Tasks"""

#------------------------------------------------------------
#first table
#------------------------------------------------------------

class Tasks(models.Model):
    morning = models.TextField()  # morning is a column in this table
    afternoon = models.TextField()
    evening = models.TextField()
    author = models.ForeignKey(   #this column carries the foriegn key
        User,
        on_delete=models.CASCADE, #delete task if user is deleted
        related_name='author_name'
    )
