from PIL import Image, ImageDraw


img = Image.new('RGBA', (400, 200), 'green')

idraw = ImageDraw.Draw(img)
idraw.rectangle((20, 20, 100, 100), fill='white')

img.save('images/holst1.png')
img.show()


# 2) 
img2 = Image.new('RGBA', (400, 200), 'green')

idraw2 = ImageDraw.Draw(img2)
idraw2.ellipse((80, 80, 200, 200), fill='white')

img2.save('images/holst2.png')
img2.show()