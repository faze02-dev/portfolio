from django.db import models

class Message(models.Model):
    full_name = models.CharField(max_length=100,blank=False, null=False)
    phone = models.CharField( max_length=200,blank=False, null=False)
    email = models.EmailField()
    Message = models.TextField()

    def _str_(self):
        return self.full_name
