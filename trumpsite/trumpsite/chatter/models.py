from django.db import models
import uuid
import datetime


# Create your models here.
class User(models.Model):
    """
    Model representing the chat profile.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    contents = models.CharField(max_length=30, help_text="Enter your first name.", default="Joe")
    name = models.CharField(max_length=30, help_text="Enter your last name.", default="Schmo")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.id
