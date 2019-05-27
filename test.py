#!/usr/bin/python3

from datetime import datetime
print('Test: ' + str(datetime.now()))

try:
  from inky import InkyPHAT
except ImportError:
  print('InkyPHAT not imported!')

try:
  from PIL import Image, ImageFont, ImageDraw
except ImportError:
  print('PIL modules not imported!')

try:
  from font_source_sans_pro import SourceSansPro
except ImportError:
  print('Font not imported!')


