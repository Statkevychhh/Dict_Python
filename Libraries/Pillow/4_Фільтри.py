from PIL import Image, ImageFilter


img = Image.open('images/picture.png')

blurred_img = img.filter(ImageFilter.BLUR)
blurred_img.save('images/blurred.png')
blurred_img.show()

contour_img = img.filter(ImageFilter.CONTOUR)
contour_img.save('images/contoured.png')
contour_img.show()