from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

def timeStamper(currentTime, picName):
    timeStampMsg = currentTime.strftime("%Y.%m.%d - %H:%H:%S")
    img = Image.open(picName)
    I1 = ImageDraw.Draw(img)
    [l,w] = img.size
    font = ImageFont.truetype("impact.ttf", size=48)
    I1.text((0.025*l, 0.9*w), timeStampMsg, fill=(255,0,0),font=font)
    img.save(picName)