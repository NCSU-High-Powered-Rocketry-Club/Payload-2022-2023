from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
# import deeppyer, asyncio
import datetime

def grassless(image: Image):
    matrix = (1,0,0,0,
            0,0,0,0,
            0,0,1,0)
    image = image.convert("RGB", matrix)
    return image

def meme(image: Image):
    height, width = image.size
    I1 = ImageDraw.Draw(image)
    meme_font = ImageFont.truetype('impact.ttf', 200)
    I1.text((0.2*width, 0.1*height),'BOTTOM TEXT', fill=(57,255,20), font=meme_font)
    return image

#async def fry(image: Image,x):
    # Fix (installing deeppyer takes forever
    # image = await deeppyer.deepfry(image)
    #return image
    #image.save(f'fried{x}.jpg')
    #print("hi")

def rotate180(image: Image,x):
    image_data = image.rotate(180)
    # image_data.save('rotated_%d.jpg' % x)
    return image_data

def blackandwhite(image: Image,x):
    bnw = image.convert("1")
    return bnw

def timestamp(image: Image):
    height, width = image.size
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    I1 = ImageDraw.Draw(image)
    I1.text((0.2*width, 0.1*height),'BOTTOM TEXT', fill=(0,0,0), font=meme_font)
