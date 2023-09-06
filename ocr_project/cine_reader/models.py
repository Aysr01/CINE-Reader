from django.db import models
# Create your models here.
class Image(models.Model):
    recto = models.ImageField(upload_to="static/", null=True)
    verso = models.ImageField(upload_to="static/", null=True)
    rot = models.CharField(max_length=100, null=True, default="0,0")