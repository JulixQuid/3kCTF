

from PIL import Image
import numpy as np

# load the image
image = Image.open('SHIFT.png')
# convert image to numpy array
data = np.asarray(image)
print(type(data))
# summarize shape
print(data.shape)

red, green, blue = image.split()
# create Pillow image
image2 = Image.fromarray(data)
print(type(image2))

# summarize image details
print(image2.mode)
print(image2.size)
def rotation(img_red,rot=1):
    img_red2= img_red.copy()
    for i in range(len(img_red)):
        img_red2[i] = np.roll(img_red[i],i*rot)
    return img_red2

uax = rotation(img_red,6)
image2 = Image.fromarray(uax)
image2.save('uax.png')