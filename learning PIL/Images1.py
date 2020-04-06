from PIL import Image

catIm = Image.open('zophie.png')

im = Image.new('RGBA', (100, 200), 'PURPLE')
im.save('purpleimage.png')

im2  = Image.new('RGBA', (300, 300))
im2.save('transparent.png')

faceIm = catIm.crop((335, 345, 565, 560))
faceIm.save('cropped.png')

catCopy = catIm.copy()

catCopy.paste(faceIm, (0, 0))
catCopy.paste(faceIm, (400, 500))
catCopy.save('catCopy.png')

catImWidth, catImHeight = catIm.size
faceWidth, faceHeight = faceIm.size
catCopy2 = catIm.copy()

for x in range(0, catImWidth, faceWidth):
    for y in range(0, catImHeight, faceHeight):
        catCopy2.paste(faceIm, (x, y))

catCopy2.save('tiled.png')

width, height = catIm.size

quater = catIm.resize(((int(width/2)), (int(height/2))))
quater.save('quatersizedIm.png')

sv = catIm.resize((width, height+300))
sv.save('streched.png')

catIm.rotate(90).save('rotated90.png')
catIm.rotate(6).save('rotated6.png')
catIm.rotate(6, expand = True).save('rotated6Expanded.png')

catIm.transpose(Image.FLIP_LEFT_RIGHT).save('flippedVertical.png')
catIm.transpose(Image.FLIP_TOP_BOTTOM).save('flippedHorizontal.png')




