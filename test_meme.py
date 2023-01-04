from PIL import Image
from PIL import ImageDraw
import deeppyer, asyncio

async def fry():
    img = Image.open('pic.jpg')
    img = await deeppyer.deepfry(img)
    img.save('fried.jpg')

loop = asyncio.get_event_loop()
loop.run_until_complete(fry())