from PIL import Image, ImageEnhance


def img_resizer_and_watermark_add(image_uploaded, width, height, watermark, opacity):
    tuple_img_with_param = image_resize(image_uploaded, width, height)
    resized_img_on_transp_layer, checked_img_size = tuple_img_with_param
    resized_img_with_watermark = put_watermark(resized_img_on_transp_layer, watermark,
                                               opacity, checked_img_size)
    return resized_img_with_watermark


def image_resize(image_uploaded, width, height):
    """Resizes the image and saves it to the path_to_save.
    Use compare_width_height() .
    If required width and height aren't equal to resized image, leave transparent spase
    around image.
    
    """
    image = Image.open(image_uploaded).convert('RGBA')
    image_width, image_height = image.size
    
    checked_img_size = compare_width_height(width, height, image_width, image_height)
    image_width, image_height = checked_img_size
    
    resized_img_on_transp_layer = Image.new('RGBA', (width, height), (0,0,0,0))
    resized_image = image.resize((int(image_width), int(image_height)))
    position = (int((width - image_width)/2), int((height - image_height)/2))
    resized_img_on_transp_layer.paste(resized_image, position)
    return resized_img_on_transp_layer, checked_img_size


def compare_width_height(width, height, image_width, image_height):
    """Compare required size(width,height) of image with initial size(image_width, image_height).
    Return decreased width and height  with saved proportions.
    If initial size of image is already less than required - do nothing.
    
    """
    if (width <= image_width and height <= image_height):
        if image_width >= image_height:
            image_height = (image_height * width) / image_width
            image_width = width
        else:
            image_width = (image_width * height) / image_height
            image_height = height
    elif width < image_width and height > image_height:
        image_height = (image_height * width) / image_width
        image_width = width
    elif width > image_width and height < image_height:
        image_width = (image_width * height) / image_height
        image_height = height
    return int(image_width),int(image_height)


def put_watermark(resized_img_on_transp_layer, watermark, opacity, checked_img_size):
    """Adds a watermark image to the input picture."""
    
    watermark = Image.open(watermark)
    if watermark.mode != 'RGBA':
        watermark = watermark.convert('RGBA')
    alpha = watermark.split()[3]
    # reduce the brightness or the 'alpha' band
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    watermark.putalpha(alpha)
    image = resized_img_on_transp_layer
    if image.mode != 'RGBA':
        image = image.convert('RGBA')
    # use compare_width_height() to but watermark only on image, avoiding transparent space
    checked_watermark_size = compare_width_height(checked_img_size[0], checked_img_size[1],
                                                  watermark.size[0], watermark.size[1])
    watermark = watermark.resize(checked_watermark_size)
    layer = Image.new('RGBA', image.size, (0,0,0,0))
    position = (int((image.size[0]-watermark.size[0])/2),int((image.size[1]-watermark.size[1])/2))
    layer.paste(watermark, position)
    resized_img_with_watermark = Image.composite(layer, image, layer)
    return resized_img_with_watermark
