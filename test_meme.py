from PIL import Image
from PIL import ImageDraw
import deeppyer

#def applyfilter(): # This calls imageFilter module
#    import imageFilter
#    image = Image.open('pic.jpg')
#    image_data = image.load()
#    height,width = image.size
#    imageFilter.meme(image, height, width) # This is a placeholder, replace w random number generator
#    image.show()

#def applyfilter(): # This calls imageFilter module
#    import imageFilter
#    image = Image.open('pic.jpg')
#    image_data = image.load()
#    height,width = image.size
#    imageFilter.grassless(image, image_data, height, width) # This is a placeholder, replace w random number generator
#    image.show()
#applyfilter()

image = Image.open('pic.jpg')
image_data = image.load()

def fry(image):
    image = deeppyer.deepfry(image)
    image.show()
    image.save('fried.jpg')

fry(image)