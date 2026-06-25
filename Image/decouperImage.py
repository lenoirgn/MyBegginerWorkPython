from PIL import Image, ImageDraw

img = Image.open("photo.png")
partie = img.crop((50, 30, 200, 150))

img.paste(partie, (10, 30))
p=img.getpixel((10, 30))
print(p)