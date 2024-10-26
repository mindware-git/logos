from PIL import Image

filename = "Logo.png"
img = Image.open(filename)
img.save("favicon.ico", sizes=[(16, 16)])
