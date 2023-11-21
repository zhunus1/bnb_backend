import os
from django.core.exceptions import ValidationError

def validate_image(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.png', '.jpg']
    limit = 5 * 1024 * 1024

    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MiB.')


def validate_presentation(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf']
    limit = 20 * 1024 * 1024

    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MiB.')