import os
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from PIL import Image

def validate_banner(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.png', '.jpg']
    limit = 5 * 1024 * 1024

    if not ext.lower() in valid_extensions:
        raise ValidationError(_('Данный формат не поддерживается.'))
    if value.size > limit:
        raise ValidationError(_('Файл слишком огромный. Максимальный размер 5 MB.'))

    # Additional validation for a square image with a maximum size of 1200x1200
    try:
        img = Image.open(value)
        width, height = img.size
        max_size = 2400

        if width <= height:
            raise ValidationError(_('Изображение должно быть в альбомном формате.'))

        if width > max_size or height > max_size:
            raise ValidationError(_('Изображение не должно превышать размер 2400 x 1256 пикселей.'))

    except Exception as e:
        # Handle image processing errors
        raise ValidationError(_('Ошибка! Попробуйте снова: %s' % str(e)))
