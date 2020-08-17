from turtle import *
import random

wn=Screen()
wn.tracer(0)
wn.bgcolor('black')
pensize(.05)
speed(0)
penup()
pencolor('cyan')
(x,y)=pos()
height=window_height()
width=window_width()
A=(0,height/4)
B=(-width/4,-height/4)
C=(width/4,-height/4)
while True:
    num=random.randint(1,9)
    if num in [1,2,3]:
        setpos((x+A[0])/2,(y+A[1])/2)
        (x,y)=pos()
        goto(x,y)
        dot()
    elif num in [4,5,6]:
        setpos((x+B[0])/2,(y+B[1])/2)
        (x,y)=pos()
        goto(x,y)
        dot()
    else:
        setpos((x+C[0])/2, (y+C[1])/2)
        (x,y)=pos()
        goto(x,y)
        dot()
    wn.update()

mainloop()