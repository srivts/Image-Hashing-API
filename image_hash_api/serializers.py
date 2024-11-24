from rest_framework import serializers
from .models import ImageDetail

class ImageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageDetail
        fields = ['id', 'image_url', 'md5_hash', 'phash', 'image_name']  # Ensure image_name is in fields if required
