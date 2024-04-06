from PIL import Image


img = Image.open('images/picture.png')

r_img = img.rotate(180)
r_img.save('images/rotated.png')
r_img.show()