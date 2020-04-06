from PIL import Image, ImageDraw
im = Image.new('RGBA', (200, 200), 'WHITE')
draw = ImageDraw.Draw(im)

draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill = 'black')
draw.rectangle((20, 30, 60, 80), fill = 'blue')
draw.ellipse((120, 30, 160, 80), fill = 'red')
draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)), fill = 'brown')

for i in range(100, 200, 10):
    draw.line([(i, 0), (200, i - 100)], fill='green')


im.save('Drawing.png')
