# profile, covere and license files validator
from django.core.exceptions import ValidationError
import os

def allow_only_images_validators(value):
    ext = os.path.splitext(value.name)[1]  # cover-image.jpg
    print(ext)
    valid_extensions = ['.png', '.jpg', '.jpeg'] # i can change it as any extension (csv and so on)
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsopported file extension. Allowed exntensions: ' +str(valid_extensions))