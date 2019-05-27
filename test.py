#!/usr/bin/python3

import csv
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

#-------------------------LOAD CSV FILE

with open('canon_texts.csv') as csvfile:
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
  topline1= head_nums[td]+ ' ' +heads[td].upper()
  topline2= ' [' +app_nums[td]+' ' +pos_negs[td]+'] '+times[td]
  message=  topline1 + topline2 +'\n'+text
  return message

message= current()
print(message) #Should print to cron.log
print('End test\n')

