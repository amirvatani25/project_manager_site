from django.db import models
from  django.contrib.auth.models import User
import uuid
from django.core.validators import RegexValidator
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , null=True , blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    phoneNumberRegex = RegexValidator(regex=r"^0\d{8,10}$")
    phone_number = models.CharField(validators=[phoneNumberRegex], max_length=11)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/',
                                      default="profiles/user-default.png")
    create = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True,
                          editable=False)
    def __str__(self):
        return str(self.user.username)