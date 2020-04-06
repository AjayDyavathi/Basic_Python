from PIL import ImageColor
print(ImageColor.getcolor('gray', 'RGBA'))
from PIL import Image
catIm = Image.open('zophie.png')
print(catIm.size)
width, height = catIm.size
print(catIm.format)
print(catIm.format_description)
catIm.save('zophie.jpg')
