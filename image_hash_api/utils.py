import hashlib
from PIL import Image
import imagehash

def generate_hashes(image_file):
    """
    Generate perceptual hash (phash) and md5 hash for an image.

    Args:
        image_file: The image file for which hashes are to be generated.

    Returns:
        tuple: phash (str), md5 (str)
    """
    # Generate md5 hash
    md5_hash = hashlib.md5(image_file.read()).hexdigest()
    image_file.seek(0)  # Reset the file pointer to the beginning

    # Generate perceptual hash
    image = Image.open(image_file)
    phash = str(imagehash.phash(image))

    return phash, md5_hash
