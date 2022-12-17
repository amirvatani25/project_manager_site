
from django.db import models
import uuid
from users.models import Profile

# Create your models here.
class Project(models.Model):
    owner = models.ForeignKey(Profile, null=True , blank=True , on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    featured_image = models.ImageField( null=True , blank=True, default="default.jpg")
    project = models.FileField(upload_to='projects/')

    create = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['create']
