from PIL import Image
from PIL import ImageDraw
import deeppyer, asyncio

def grassless(image,image_data,height,width):
    for loop1 in range(height):
        for loop2 in range(width):
            r,g,b = image_data[loop1,loop2]
            image_data[loop1,loop2] = r,0,b
            image.save('grassless.jpg')

def meme(image,height,width):
    I1 = ImageDraw.Draw(image)
    I1.text((0.25*height, 0.25*width),"poo", fill=(255,0,0))
    image.save('meme.jpg')

async def fry(image):
    image = await deeppyer.deepfry(image)
    image.save('fried.jpg')