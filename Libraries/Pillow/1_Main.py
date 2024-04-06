from PIL import Image


img = Image.open('images/picture.png')
img.show()

print(img.size)
print(img.format)
print(img.mode)
print(img.histogram)


# 2)
img.thumbnail((200, 200))
img.save('images/mini_img.png')
img.show()