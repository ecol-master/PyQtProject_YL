from PIL import Image
import os

def save_image_in_folder(file_name):
    im = Image.open(file_name)
    width1, height1 = im.size[0], im.size[1]
    if width1 > height1:
        height1 = 371 * (height1 / width1)
        width1 = 371
    else:
        width1 = 251 * (height1 / width1)
        height1 = 251
    name = str(file_name).split('/')[-1]
    im_resized = im.resize((int(round(width1)), round(height1)))
    im_resized.save(f"images/{name}")
    return name