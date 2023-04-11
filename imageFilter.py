from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
# import deeppyer, asyncio
import datetime

def grassless(image: Image):
    width, height = image.size
    for y in range(height):
        for x in range(width):
            r,_,b = image[y][x]
            image[y][x] = r,0,b
    return image

def meme(image: Image):
    height, width = image.size
    I1 = ImageDraw.Draw(image)
    meme_font = ImageFont.truetype('impact.ttf', 200)
    I1.text((0.2*width, 0.1*height),'BOTTOM TEXT', fill=(0,0,0), font=meme_font)
    return image

#async def fry(image: Image,x):
    # Fix (installing deeppyer takes forever
    # image = await deeppyer.deepfry(image)
    #return image
    #image.save(f'fried{x}.jpg')
    #print("hi")

def rotate180(image: Image,x):
    image_data = image.rotate(180)
    image_data.save('rotated_%d.jpg' % x)

async def blackandwhite(image: Image,x):
    bnw = image.convert("1")
    return bnw
if __name__ == "__main__":
    pic2filter = Image.open("MikeWhenHe.png")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fry(pic2filter, 5))

def timestamp(image: Image):
    height, width = image.size
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    I1 = ImageDraw.Draw(image)
    I1.text((0.2*width, 0.1*height),'BOTTOM TEXT', fill=(0,0,0), font=meme_font)
