from PIL import Image
from PIL import ImageDraw

def timeStamper(currentTime, picName):
    timeStampMsg = currentTime.strftime("%Y.%m.%d - %H:%H:%S")
    img = Image.open(picName)
    I1 = ImageDraw.Draw(img)
    [l,w] = img.size
    I1.text((0.025*l, 0.9*w), timeStampMsg, fill=(255,0,0))
    img.save(picName)



