from PIL import Image


img = Image.open('images/picture.png')

crop_img = img.crop((100, 200, 300, 400))
crop_img.save('images/cropped.png')
crop_img.show()