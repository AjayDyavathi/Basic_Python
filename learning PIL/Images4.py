from PIL import Image, ImageDraw, ImageFont
import os
im = Image.new('RGBA', (200, 200), 'WHITE')
draw = ImageDraw.Draw(im)
draw.text((20, 150), 'HELLO', fill = 'PURPLE')
fontsFolder = '/Library/Fonts'
arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)
draw.text((100, 150), 'Ajay', fill = 'gray', font = arialFont)
im.save('text.png')
