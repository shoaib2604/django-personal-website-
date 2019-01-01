from django.db import models

# Create your models here.
class Contact(models.Model):
    Email=models.EmailField()
    Subject=models.CharField(max_length=200)
    message=models.TextField()

    def __str__(self):
        return self.Email
