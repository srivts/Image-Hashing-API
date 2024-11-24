from django.urls import path
from .views import (
    ImageDetailList,
    ImageDetailRetrieve,
    ImageDetailCreate,
    ImageDetailUpdate,
    ImageDetailDelete,
)

urlpatterns = [
    path('images/', ImageDetailList.as_view(), name='image_list'),  # List all images
    path('images/<int:pk>/', ImageDetailRetrieve.as_view(), name='image_detail'),  # Retrieve image by ID
    path('images/create/', ImageDetailCreate.as_view(), name='image_create'),  # Create image record
    path('images/<int:pk>/update/', ImageDetailUpdate.as_view(), name='image_update'),  # Update image record
    path('images/<int:pk>/delete/', ImageDetailDelete.as_view(), name='image_delete'),  # Delete image record
]
