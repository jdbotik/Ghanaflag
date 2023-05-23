#JDK the Creator
#import turtle for drawing and import time to hold when needed
import turtle
import time

gh =turtle.Turtle()
#red, yellow, green
y = 300


#this while loop draws the 3 parts fpr the 3 colors
while y > -81:
    gh.penup()
    gh.goto(-260,y)
    gh.lt(90)
    gh.pendown()
    gh.fd(160)
    gh.rt(90)
    gh.begin_fill()
    
    #to fill the color in every shape
    if y == 300:
        j= 'red'
    elif y == 300-160:
        j = 'yellow'
    elif y == 300 -(160*2):
        j = 'green'
    else:
         j = 'black'
    gh.fillcolor(j)
    
    #drawing the upper part of the wave
    for i in range(10):
        gh.fd(10)
        gh.lt(2)
    for i in range(20):
        gh.fd(10)
        gh.rt(2)
    for i in range(26):
        gh.lt(2)
        gh.fd(10)
        
   #turning and moving down     
    gh.lt(58)
    gh.bk(160)
    gh.rt(58)
    #reversing   
    for i in range(26):
        gh.bk(10)
        gh.rt(2)
    for i in range(20):
        gh.lt(2)
        gh.bk(10)
    for i in range(10):
        gh.rt(2)
        gh.bk(10)
    gh.end_fill()
    y-=160


#star        
#moving to the center
gh.penup()
gh.goto(-30,250)
gh.pendown()
#begin to fill the star with black
gh.begin_fill()
gh.fillcolor('black') 
for i in range(5):
    gh.fd(40)
    gh.lt(72)
    gh.fd(40)
    gh.rt(144)
    
gh.end_fill()


#drawing the stand with base
gh.begin_fill()
gh.penup()
gh.goto(-260,-550)
gh.pendown()
gh.lt(90)
gh.fd(1040)
gh.lt(90)
gh.fd(10)
gh.lt(90)
gh.fd(1040)
gh.rt(90)
gh.fd(40)
gh.lt(90)
gh.fd(30)
gh.lt(90)
gh.fd(90)
gh.lt(90)
gh.fd(30)
gh.lt(90)
gh.fd(40)
gh.end_fill()
    
#make the turtke disappear for a while
gh.hideturtle()
time.sleep(10)