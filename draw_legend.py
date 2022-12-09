# Imports PIL module
from PIL import Image, ImageDraw
from colour import Color
colors = list(  Color("red").range_to(Color("blue"), 100))
 
# creating a image object (new image object) with
# RGB mode and size 200x200
im = Image.new(mode="RGB", size=(30, 200))
draw = ImageDraw.Draw(im)
count = 0
# draw.rectangle([ (0, 0), (30, 200) ], fill=True, outline=None, width=10)
for color in colors:
    r = color.get_red()
    g = color.get_green()
    b = color.get_blue()
    
    draw.rectangle([ (0, count * 2), (30, (count + 1) * 2) ], fill=color.get_hex(), outline=None, width=10)
    count += 1
 
# This method will show image in any image viewer
im.show()