
# using to test udacity asciichan


from django.db import models
import datetime
from django.utils import timezone



class Art(models.Model):
    title = models.CharField(max_length=500)
    art = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    coords = models.CharField(max_length=200)

    def __str__(self):
        return self.title

