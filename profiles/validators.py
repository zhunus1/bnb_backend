import os
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from PIL import Image

def validate_image(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.png', '.jpg']
    limit = 5 * 1024 * 1024

    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 5 MiB.')

    # Additional validation for a square image with a maximum size of 1200x1200
    try:
        img = Image.open(value)
        width, height = img.size
        max_size = 1200

        if width != height:
            raise ValidationError(_('The image must be square.'))

        if width > max_size or height > max_size:
            raise ValidationError(_('The image must be no larger than 1200x1200 pixels.'))

    except Exception as e:
        # Handle image processing errors
        raise ValidationError(_('Error processing the image: %s' % str(e)))


def validate_presentation(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf']
    limit = 20 * 1024 * 1024

    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MiB.')