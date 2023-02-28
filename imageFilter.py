from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import deeppyer, asyncio

async def grassless(image, x):
    image_data = image.load()
    height, width = image.size
    for loop1 in range(height):
        for loop2 in range(width):
            r,g,b = image_data[loop1,loop2]
            image_data[loop1,loop2] = r,0,b
    return image

async def meme(image,x):
    height, width = image.size
    I1 = ImageDraw.Draw(image)
    meme_font = ImageFont.truetype('impact.ttf', 200)
    I1.text((0.2*width, 0.1*height),'BOTTOM TEXT', fill=(0,0,0), font=meme_font)
    return image

async def fry(image,x):

    image = await deeppyer.deepfry(image)
    #return image
    image.save(f'fried{x}.jpg')
    #print("hi")

def rotate180(image,x):
    image = image.rotate(180)
    image.save('rotated_%d.jpg' % x)

async def blackandwhite(image,x):
    bnw = image.convert("1")
    return bnw
if __name__ == "__main__":
    pic2filter = Image.open("capture_pinky_0.jpg")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fry(pic2filter, 3))
    