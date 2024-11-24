from django.db import models

class ImageDetail(models.Model):
    image_url = models.URLField(max_length=200)
    md5_hash = models.CharField(max_length=128)
    phash = models.CharField(max_length=128)
    image_name = models.CharField(max_length=255, default="")  # Add this field if you need it

    def __str__(self):
        return self.image_url
