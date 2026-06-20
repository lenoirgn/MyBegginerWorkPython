from PIL import Image,ImageDraw

#img = Image.new("RGBA", (500, 300), (25,45,25))
img=Image.open("image_rouge.png")

draw = ImageDraw.Draw(img)
#draw.text((250, 250), "Bonjour Python", fill="black")

#img.show()
img.save("bonjour.png")

#draw.rectangle((100, 50, 400, 250), outline="black", width=3)
#img.show()

# draw.line((50, 50, 450, 250), fill="red", width=3)
# img.show()

# draw.ellipse((100, 50, 300, 250), outline="blue", width=3)
# img.show()


# draw.arc((100, 50, 300, 250), start=0, end=180, fill="red")
# img.show()

# draw.point((250, 150), fill="yellow")
# img.show()

# draw.chord((100, 50, 300, 250), 0, 180, fill="green")
# img.show()

draw.pieslice((100, 50, 300, 250), 0, 90, fill="orange")
img.show()
