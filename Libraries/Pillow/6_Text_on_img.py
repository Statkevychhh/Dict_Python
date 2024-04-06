from PIL import Image, ImageDraw, ImageFont


img = Image.new('RGBA', (400, 200), 'gray')
idraw = ImageDraw.Draw(img)

idraw.rectangle((20, 20, 100, 100), fill = 'yellow')

headline = ImageFont.truetype('arial.ttf', size = 30)
text = 'Hello World'
idraw.text((110, 20), text, font = headline)

img.save('images/with_text.png')
img.show()