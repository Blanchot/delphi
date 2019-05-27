#!/usr/bin/python3

from datetime import datetime
print('Test: ' + str(datetime.now()))

try:
  from inky import InkyPHAT
  print('InkyPHAT imported!')
except:
  print('InkyPHAT not imported!')

try:
  from PIL import Image, ImageFont, ImageDraw
  print('PIL modules imported!')
except:
  print('PIL modules not imported!')

try:
  from font_source_sans_pro import SourceSansPro
  print('Font: SourceSansPro imported!')
except:
  print('Font not imported!')

print('End test\n')

