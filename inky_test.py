from inky import InkyPHAT
inky_display = InkyPHAT("red")
inky_display.set_border(inky_display.WHITE)

from PIL import Image, ImageFont, ImageDraw
img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

'''
from font_fredoka_one import FredokaOne
font = ImageFont.truetype(FredokaOne, 22)
'''

from font_source_sans_pro import SourceSansPro
font= ImageFont.truetype(SourceSansPro, 12)

message = "Hello, World!"
w, h = font.getsize(message)
x = (inky_display.WIDTH / 2) - (w / 2)
y = (inky_display.HEIGHT / 2) - (h / 2)

draw.text((x, y), message, inky_display.RED, font)
inky_display.set_image(img)
inky_display.show()
