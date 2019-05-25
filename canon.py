'''Canon.py Version 1: 25 May 2019'''

import csv
from datetime import datetime

#-------------------------SET UP INKYPHAT
from inky import InkyPHAT
inky_display = InkyPHAT("red")
inky_display.set_border(inky_display.WHITE)

from PIL import Image, ImageFont, ImageDraw
img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

from font_source_sans_pro import SourceSansPro
font= ImageFont.truetype(SourceSansPro, 12)

#-------------------------LOAD CSV FILE

with open('canon.csv') as csvfile:
  readCSV= csv.reader(csvfile, delimiter=';')
  head_nums= []
  heads= []
  app_nums= []
  pos_negs= []
  times= []
  texts= []
  
  for row in readCSV:
    head_num= row[0]
    head= row[1]
    app_num= row[2]
    pos_neg= row[3]
    time= row[4]
    text= row[5]   
    
    head_nums.append(head_num)
    heads.append(head)
    app_nums.append(app_num)
    pos_negs.append(pos_neg)
    times.append(time)
    texts.append(text)


#-------------------------CREATE AND DRAW MESSAGE
def current():
  nu= datetime.now()
  nu= nu.strftime('%d/%m %p')
  td= times.index(nu)
  text= texts[td]
  text= text.replace("\\n","\n",1) #need to add this because csv file weirdness (check using repr())
  topline1= head_nums[td]+ ' ' +heads[td].upper()
  topline2= ' [' +app_nums[td]+' ' +pos_negs[td]+'] '+times[td]
  message=  topline1 + topline2 +'\n'+text
  return message

message= current()
x= 0
y= 0
draw.text((x, y), message, inky_display.BLACK, font)
inky_display.set_image(img)
inky_display.show()

