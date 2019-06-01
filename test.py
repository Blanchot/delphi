#!/usr/bin/python3

'''TEST.PY
25 May 2019: First commit
27 May 2019: Added color differentiation
30 May 2019: Added phase indication + support for day/night background + 'fathomings'
30 May 2019: Added day/night background and 'fathomings'
'''

import csv
from datetime import datetime

#print(datetime.now()) #primarily for testing -> cron.log

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
#with open('canon_texts_copy.csv') as csvfile: #FOR TESTING
with open('/home/pi/delphi/canon_texts.csv') as csvfile: #need full path for cron to work!
  readCSV= csv.reader(csvfile, delimiter=';')
  
  tetapp_nums= [] #list of tetragram and appraisal numbers: 01/1 to 81/9
  tet_names= [] #list of corresponding tetragram names
  app_nums= [] #list of appraisal numbers: 001 to 729 (or 731 in case of leap years)
  pos_negs= [] #list of + for day and - for night (not necessary as this can be surmised from times)
  times= [] #list of daytimes in the form: dd/mm AM or PM
  app_txts= [] #list of appraisal texts
  com_txts= [] #list of comment texts (fathomings)
  
  for row in readCSV:
    tetapp_num= row[0]
    tet_name= row[1]
    app_num= row[2]
    pos_neg= row[3]
    time= row[4]
    #row[5] is used to indicate edits to original text to accomodate smaller screen
    app_txt= row[6]
    com_txt= row[7]
    
    tetapp_nums.append(tetapp_num) #col [0]
    tet_names.append(tet_name) #col [1]
    app_nums.append(app_num) #col [2]
    pos_negs.append(pos_neg) #col [3]
    times.append(time) #col [4]
    app_txts.append(app_txt) #col [6]
    com_txts.append(com_txt) #col [7]


#-------------------------FIND AND PARSE DATA TO CREATE MESSAGE
def current():
  nu= datetime.now()
  nu= nu.strftime('%d/%m %p')
  td= times.index(nu) #get index of current date and use to create message
  
  #Parse the number part of tetapp_num for return (to later draw the tetragram)
  tet_num= int((tetapp_nums[td])[0:2])
  
  #Parse the appraisal part of tetapp_num to get the current element phase
  phase= (tetapp_nums[td])[3]
  if phase =='1' or phase =='6':
    phase= 'A' #Water or Aqua/Agua
  elif phase =='2' or phase =='7':
    phase= 'F' #Fire
  elif phase =='3' or phase =='8':
    phase= 'W' #Wood
  elif phase =='4' or phase =='9':
    phase= 'M' #Metal
  else:
    phase= 'E' #Earth
  
  #Parse app_txt and count number of newlines for composing screen 'drawing'
  app_txt= app_txts[td]
  
  #Other values to return
  pos_neg= pos_negs[td] #Pos or Neg (Yang or Yin, Day or Night)
  com_txt= com_txts[td]
  
  #Research why I need to do what I do in the two lines below
  app_txt= app_txt.replace("\\n","\n",4) #need to add this because csv file weirdness (check using repr())
  com_txt= com_txt.replace("\\n","\n",4) #need to add this because csv file weirdness (check using repr())
  
  linecount= app_txt.count('\n') + 1
  
  #Topline composition
  topline_a= tetapp_nums[td]+ ' ' +tet_names[td].upper()
  topline_b= ' [' +app_nums[td]+' ' +phase+'] '+times[td]
  topline= topline_a + topline_b +'\n'
  
  #Return tuple
  message= pos_neg, topline, app_txt, linecount, com_txt, tet_num
  
  print(topline + app_txt +'\n('+ com_txt +')') #Prints to cron.log
  return message

#-------------------------DRAW SCREEN
pos_neg, topline, app_txt, linecount, com_txt, tet_num= current()

if pos_neg =='+': #positive means day, yang, auspicious
  draw.rectangle([0,0,212,17],fill=inky_display.RED)
else:
  draw.rectangle([0,0,212,17],fill=inky_display.BLACK)
  
draw.text((1, 0), topline, inky_display.WHITE, font) #adding a bit of a buffer: 1 pixel
draw.text((0, 17), app_txt, inky_display.BLACK, font)

if linecount ==1:
  draw.text((0, 34), com_txt, inky_display.RED, font)
elif linecount ==2:
  draw.text((0, 51), com_txt, inky_display.RED, font)
elif linecount ==3:
  draw.text((0, 68), com_txt, inky_display.RED, font)
elif linecount ==4:
  draw.text((0, 85), com_txt, inky_display.RED, font)

#'''
#TETRAGRAM DRAWING CODE (draws lines in topline area )
tet_num= tet_num -1 #shifting range from 1-81 to 0-80
line1= tet_num//27
tet_num= tet_num%27
line2= tet_num//9
tet_num= tet_num%9
line3= tet_num//3
tet_num= tet_num%3
line4= tet_num//1

lines= [line1, line2, line3, line4]

y_coord= 2
for line in lines:
  if line==0: #no breaks
    draw.line((199,y_coord,209,y_coord), inky_display.WHITE)
  elif line==1: #one breaks
    draw.line((199,y_coord,203,y_coord), inky_display.WHITE)
    draw.line((205,y_coord,209,y_coord), inky_display.WHITE)
  elif line==2: #two breaks
    draw.line((199,y_coord,201,y_coord), inky_display.WHITE)
    draw.line((203,y_coord,205,y_coord), inky_display.WHITE)
    draw.line((207,y_coord,209,y_coord), inky_display.WHITE)
  y_coord= y_coord +2

#'''
 
inky_display.set_image(img)
inky_display.show()

