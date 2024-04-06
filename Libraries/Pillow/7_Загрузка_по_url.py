from PIL import Image
import requests


url = input(':::> ')
response = requests.get(url, stream = True).raw

img = Image.open(response)
img.save('images/with_url.png', 'png')
img.show()