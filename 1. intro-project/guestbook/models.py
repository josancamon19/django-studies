from django.db import models
from django.utils.timezone import now


# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=20)
    comment = models.TextField()
    date_added = models.DateTimeField(default=now())

    def __str__(self):
        return '<Name: {}, ID: {}>'.format(self.name, self.id)
