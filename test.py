import turtle
import math
import random
wn = turtle.Screen()
wn.bgcolor('black')
Numan = turtle.Turtle()
Numan.speed(0)
Numan.color('white')
rotate=int(360)
def LageSirkler(t,size):
    for i in range(10):
        t.circle(size)
        size=size-4
def TegnSpesial(t,size,repeat):
  for i in range (repeat):
    LageSirkler(t,size)
    t.right(360/repeat)
TegnSpesial(Numan,100,10)
Marie = turtle.Turtle()
Marie.speed(0)
Marie.color('yellow')
rotate=int(90)
def LageSirkler(t,size):
    for i in range(4):
        t.circle(size)
        size=size-10
def TegnSpesial(t,size,repeat):
    for i in range (repeat):
        LageSirkler(t,size)
        t.right(360/repeat)
TegnSpesial(Marie,100,10)
MaiLill = turtle.Turtle()
MaiLill.speed(0)
MaiLill.color('blue')
rotate=int(80)
def LageSirkler(t,size):
    for i in range(4):
        t.circle(size)
        size=size-5
def LageSirkler(t,size,repeat):
    for i in range (repeat):
        LageSirkler(t,size)
        t.rig
    ht(360/repeat)
TegnSpesial(MaiLill,100,10)
Arvid = turtle.Turtle()
Arvid.speed(0)
Arvid.color('orange')
rotate=int(90)
def LageSirkler(t,size):
    for i in range(4):
        t.circle(size)
        size=size-19
def TegnSpesial(t,size,repeat):
    for i in range (repeat):
        LageSirkler(t,size)
        t.right(360/repeat)
TegnSpesial(Arvid,100,10)
Hei = turtle.Turtle()
Hei.speed(0)
Hei.color('pink')
rotate=int(90)
def LageSirkler(t,size):
    for i in range(4):
        t.circle(size)
        size=size-20
def TegnSpesial(t,size,repeat):
    for i in range (repeat):
        LageSirkler(t,size)
        t.right(360/repeat)
TegnSpesial(Hei,100,10)
