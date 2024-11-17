from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class Usermanager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError("Email is required")
        if not password:
            raise ValueError("Password is required")
        
        user = self.model(email=self.normalise_email(email))
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to="profile_photos/", null=True, blank=True)

    objects = Usermanager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    



