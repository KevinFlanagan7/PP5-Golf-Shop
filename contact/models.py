from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact message from {self.name} at {self.email}"