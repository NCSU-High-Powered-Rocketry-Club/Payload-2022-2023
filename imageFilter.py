from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import deeppyer, asyncio

def grassless(image):
    image_data = image.load()
    height, width = image.size
    for loop1 in range(height):
        for loop2 in range(width):
            r,g,b = image_data[loop1,loop2]
            image_data[loop1,loop2] = r,0,b
            image.save('grassless.jpg')

def meme(image,x):
    height, width = image.size
    I1 = ImageDraw.Draw(image)
    meme_font = ImageFont.truetype('impact.ttf', 200)
    I1.text((0.2*width, 0.1*height),'BOTTOM TEXT', fill=(0,0,0), font=meme_font)
    image.save('meme.jpg')

async def fry(image,x):
    #image = await deeppyer.deepfry(image)
    #image.save('fried.jpg')
    print("hi")

def rotate180(image,x):
    image = image.rotate(180)
    image.save('rotated_%d.jpg' % x)

def blackandwhite(image,x):
    bnw = image.convert("1")
    return bnw