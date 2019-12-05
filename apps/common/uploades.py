import os
from PIL import Image
from django.conf import settings
from django.core.exceptions import ValidationError


ALLOWED_EXTENSIONS = getattr(settings,'ALLOWED_EXTENSIONS')
ALLOWED_MIME_TYPES = getattr(settings,'ALLOWED_MIME_TYPES')


def get_default_avatar_url():

    if hasattr(settings,'DEFAULT_AVATAR_URL'):
        return getattr(settings,'DEFAULT_AVATAR_URL')
    return None
    


def upload_loc(instance,file_obj):
    file_ext = file_obj.split('.')[-1].lower()
    file = '{}.{}'.format(instance.owner.username,file_ext)
    return os.path.join('dp',file)



def validate_file_mimetype(uploaded_file_obj):
    # use : Model attr is <FileField>
    if uploaded_file_obj.content_type not in ALLOWED_MIME_TYPES:
        raise ValidationError("Uploaded file type is not allowed")



def validate_uploaded_file_size_and_extension(uploaded_file_obj):
    try:
        validate_file_extention(uploaded_file_obj)
        validate_file_size(uploaded_file_obj)
    except ValidationError as e:
        return e
    return True


    

def validate_file_size(uploaded_file_obj):
    upload_limit = settings.AVATAR_UPLOAD_SIZE_LIMIT * 1024 # 1MB
    if uploaded_file_obj.size > upload_limit:
        raise ValidationError("Uploaded file size must be 1MB or less")
    return True
    	


def validate_file_extention(uploaded_file_obj):
    file_name = uploaded_file_obj.name
    file_ext = file_name.lower().split('.')[-1]
    if not file_ext in ALLOWED_EXTENSIONS:
        raise ValidationError('Uploaded file format,.{0} is not supported'.format(file_ext))
    return True





def validate_uploaded_file_dimensions(uploaded_file_obj):
    limited_ratio = 0.25
    image_obj = Image.open(uploaded_file_obj)
    image_ratio = float(min(image_obj.size)) / float(max(image_obj.size))

    min_size = max(settings.AVATAR_DIMENSION_SIZES) #250
    image_obj_dimn_size = image_obj.size #(241, 209)
    min_image_obj_dmsize = min(image_obj_dimn_size) # 209

    if min_image_obj_dmsize < min_size:
        mssg = "uploaded image must be at least,{0}'s px wide and tall".format(min_size)
        raise ValidationError(mssg)
    
    if min_image_obj_dmsize[0] * min_image_obj_dmsize[1] > 300 * 350:
        mssg = "uploaded image has big dimensions"
        raise ValidationError(mssg)

    if image_ratio < limited_ratio:
        mssg = "uploaded image ratio must not exceed {}".format(limited_ratio)
        raise ValidationError(mssg)

    # return image_obj
    return True






def validate_uploaded_file_size_extension_dimensions(uploaded_file_obj):
    try:
        validate_file_extention(uploaded_file_obj)
        validate_file_size(uploaded_file_obj)
        validate_uploaded_file_dimensions(uploaded_file_obj)
    except ValidationError as e:
        return e
    return True


def validate_image_square(file_obj):
    if not file_obj.width == file_obj.height:
        raise ValidationError("uploaded image is not a square")







