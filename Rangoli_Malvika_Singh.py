import turtle #importing turtle

turtle.screensize(canvwidth=400, canvheight=600, bg="black") #adjusting the size of the screen
pt= turtle.Turtle() #pt is for patern
sc= turtle.Turtle() #sc for screen
pt.speed(0)
radius=40
pt.pensize(1)
colour= ["deeppink","cyan","magenta","lime","hotpink","Yellow","crimson","darkblue"] #colour list
pt.penup()     #the turtle won't write now when it moves
pt.goto(0,0)
pt.pendown()    #the turtle will now write as it moves 
for x in range(10):      #printing multiple deeppink circle pattern
  pt.color(colour[0])
  for i in range(20):
    pt.circle(radius+10)
    pt.right(30)
  radius= radius + 2
for x in range(5):      #printing multiple lime green circle pattern
  pt.color(colour[3])
  for i in range(15):
    pt.circle(radius+60)
    pt.right(30)
  radius=radius + 2
for x in range(5):      #printing multiple magenta circle patern
  pt.color(colour[2])
  for i in range(15):
    pt.circle(radius+80)
    pt.right(30)
  radius=radius + 2
for x in range(5):      #printing multiple yellow circle patern
  pt.color(colour[5])
  for i in range(20):
    pt.circle(radius+130)
    pt.right(30)
  radius= radius + 1

def hex(n):
  pt.forward(n)            #function for  blue circle patern in the middle
  pt.color(colour[7])
  for _ in range(5):
    pt.left(90)
    pt.forward(n)
  pt.left(90)
pt.penup()
pt.goto(30,20)
pt.pendown()
for i in range(10):
  for _ in range(4):       #printing multiple blue circle patern in the middle
    hex(50)
    pt.left(15)

pt.penup()
pt.goto(300,0)
fr=1
pt.pendown()
for x in range(120):
  pt.color(colour[1])
  pt.forward(fr)             #printing the star at 3'0 cloclk
  pt.left(150)
  pt.left(5)
  fr +=1
pt.penup()
pt.goto(0,300)
fr=1
pt.pendown()
for x in range(120):
  pt.color(colour[4])       #printing the star at 12'0 cloclk
  pt.forward(fr)
  pt.left(150)
  pt.left(5)
  fr +=1
pt.penup()
pt.goto(-300,0)
fr=1
pt.pendown()
for x in range(120):            #printing the star at 9'0 cloclk
  pt.color(colour[1])
  pt.forward(fr)
  pt.left(150)
  pt.left(5)
  fr +=1
pt.penup()
pt.goto(0,-300)
fr=1
pt.pendown()
for x in range(120):
  pt.color(colour[4])
  pt.forward(fr)
  pt.left(150)               #printing the star at 6'0 cloclk
  pt.left(5)
  fr +=1
pt.penup()
pt.goto(300,-120)
fr=1
pt.pendown()
for x in range(120):
  pt.color(colour[6])
  pt.forward(fr)
  pt.left(120)                 #printing the patterns below the 9'0 clock
  pt.left(5)
  fr +=1
pt.penup()
pt.goto(300,120)
fr=1
pt.pendown()
for x in range(120):
  pt.color(colour[6])
  pt.forward(fr)               #printing the pattern below at 9'0 cloclk
  pt.left(120)
  pt.left(5)
  fr +=1
pt.penup()
pt.goto(-300,120)
fr=1
pt.pendown()
for x in range(120):
  pt.color(colour[6])
  pt.forward(fr)
  pt.left(120)
  pt.left(5)      #printing the patterns above the 9'0 clock
  fr +=1
pt.penup()
pt.goto(-300,-120)
fr=1
pt.pendown()
for x in range(120):
  pt.color(colour[6])
  pt.forward(fr)
  pt.left(120)       #printing the patterns below the 9'0 clock
  pt.left(5)
  fr +=1
pt.penup()
pt.goto(180,280)
fr=1
pt.pendown()
for x in range(120):
  pt.color(colour[1])
  pt.forward(fr)
  pt.left(150)
  pt.left(5)           #printing the patterns at the 1'0 clock
  fr +=1
pt.penup()
pt.goto(-180,280)
fr=1
pt.pendown()
for x in range(120):
  pt.color(colour[1])
  pt.forward(fr)          #printing the patterns at the 11'0 clock
  pt.left(150)
  pt.left(5)
  fr +=1
pt.penup()
pt.goto(-180,-280)
fr=1
pt.pendown()
for x in range(120):
  pt.color(colour[1])
  pt.forward(fr)
  pt.left(150)
  pt.left(5)          #printing the patterns at 7'0 clock
  fr +=1
pt.penup()
pt.goto(180,-280)
fr=1
pt.pendown()
for x in range(120):
  pt.color(colour[1])      #printing the patterns at 5'0 clock
  pt.forward(fr)
  pt.left(150)
  pt.left(5)
  fr +=1
turtle.done()
