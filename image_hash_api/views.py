from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from .models import ImageDetail
from .serializers import ImageDetailSerializer
from .utils import generate_hashes
import requests
from io import BytesIO
from PIL import Image
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response


# View to List all Image Details
class ImageDetailList(ListAPIView):
    """
    List all image details.
    """
    queryset = ImageDetail.objects.all()
    serializer_class = ImageDetailSerializer


# View to Retrieve a single Image Detail
class ImageDetailRetrieve(RetrieveAPIView):
    """
    Retrieve a single image detail by ID.
    """
    queryset = ImageDetail.objects.all()
    serializer_class = ImageDetailSerializer


# View to Create an Image Detail from URL
class ImageDetailCreate(CreateAPIView):
    """
    Create a new image detail from a provided image URL.
    """
    queryset = ImageDetail.objects.all()
    serializer_class = ImageDetailSerializer

    def get(self, request: Request, *args, **kwargs):
        image_url = request.query_params.get('image_url', None)

        if image_url:
            try:
                # Fetch the image from the URL
                response = requests.get(image_url)
                response.raise_for_status()

                # Open the image and verify its integrity
                image_file = BytesIO(response.content)
                try:
                    img = Image.open(image_file)
                    img.verify()  # Verify the image integrity
                except (IOError, SyntaxError):
                    raise ValidationError("Invalid image file format")

                # Reset the file pointer before processing
                image_file.seek(0)

                # Generate md5_hash and phash using the provided function
                phash, md5 = generate_hashes(image_file)

                # Default image name based on the image URL
                image_name = image_url.split("/")[-1].split("?")[0]

                # Create the image detail entry using the serializer
                image_detail = ImageDetail.objects.create(
                    md5_hash=md5, phash=phash, image_name=image_name, image_url=image_url
                )

                # Return the generated hashes and image URL in the response
                return Response({
                    "image_url": image_url,
                    "md5_hash": md5,
                    "phash": phash,
                    "image_name": image_name,
                    "status": "Success"
                })

            except requests.exceptions.RequestException as e:
                raise ValidationError(f"Failed to fetch image from URL: {str(e)}")
        else:
            return Response({"error": "No image URL provided"}, status=400)


# View to Update an Image Detail
class ImageDetailUpdate(UpdateAPIView):
    queryset = ImageDetail.objects.all()
    serializer_class = ImageDetailSerializer

    def perform_update(self, serializer):
        if 'image' in self.request.FILES:
            image_file = self.request.FILES['image']
            phash, md5 = generate_hashes(image_file)
            # If the model has image_name, save it
            serializer.save(image_name=image_file.name, md5_hash=md5, phash=phash)
        else:
            serializer.save()


# View to Delete an Image Detail
class ImageDetailDelete(DestroyAPIView):
    """
    Delete an image detail by ID.
    """
    queryset = ImageDetail.objects.all()
    serializer_class = ImageDetailSerializer
