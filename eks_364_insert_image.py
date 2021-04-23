# !/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import PhotoImage
import turtle
from turtle import Turtle, Screen, Shape

#initialisering, setter "vindu" konfigurasjon.
eksempel = turtle.Screen()
#eksempel.screensize(500, 500)
eksempel.setup(1000, 1000)                        #alternativ konfigurasjon av stage (arbeidsflate)
eksempel.title("Eks. 364, sett inn bilde.")

#eksempel.bgpic("./turtlelpg.png")

#initialisering, definerer hvor turtle starter, farge, hastighet mv.
figur = Turtle("turtle")
figur.hideturtle()
figur.penup()
figur.setposition(-200, -200)     # Starter i "Origo", for Turtle er det  midt i skjermen. 

#Same size as imported image:
#eksempel.addshape(name="./bilder/Solbergfoss_photo3364_200x150.gif",shape=None)
#figur.shape("spaceship.gif")

#Bigger image,resize:
larger = PhotoImage(file="./turtlelpg.png").zoom(3, 3)
eksempel.addshape("larger", Shape("image", larger))
figur.shape("larger")

#Lesser image, resize:
#lesser = PhotoImage(file="./turtlelpg.png").subsample(5, 5)
#eksempel.addshape("lesser", Shape("image", lesser))
#figur.shape("lesser")
figur.showturtle()

eksempel.mainloop()