from django.db import models
import uuid


# Create your models here.
class Chat(models.Model):
    """
    Model representing the chat profile.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    contents = models.CharField(max_length=30, help_text="Enter your first name.", default="")
    name = models.CharField(max_length=30, help_text="Enter your last name.", default="")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return str(self.name) + ": " + str(self.contents)

