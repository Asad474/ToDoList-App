from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class MyUser(AbstractUser):
    email = models.EmailField(unique = True, null = True)
    bio = models.TextField(
        default = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    )
    avatar = models.ImageField(null = True, default = "captain-america.jpg", verbose_name = 'Profile pic')

    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class Task(models.Model):
    user = models.ForeignKey(MyUser, on_delete = models.CASCADE)
    task = models.CharField(max_length = 100)
    complete = models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return self.task

    class Meta:
        ordering = ['-complete']    