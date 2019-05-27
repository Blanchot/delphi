#!/usr/bin/python3

'''Test.py: 27 May 2019'''

import csv
from datetime import datetime

#print(datetime.now())

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

with open('/home/pi/delphi/canon_texts.csv') as csvfile: #need full path for cron to work!
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
    text= row[6] #row[5] is to indicate edits to original text to accomodate smaller screen
    
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
  text= text.replace("\\n","\n",4) #need to add this because csv file weirdness (check using repr())
  topline-a= head_nums[td]+ ' ' +heads[td].upper()
  topline-b= ' [' +app_nums[td]+' ' +pos_negs[td]+'] '+times[td]
  topline= topline-a + topline-b +'\n'
  message= topline, appraisal
  return message

topline, appraisal= current()
#print(message) #Should print to cron.log
draw.text((0, 0), topline, inky_display.RED, font)
draw.text((0, 17), appraisal, inky_display.BLACK, font)
inky_display.set_image(img)
inky_display.show()
