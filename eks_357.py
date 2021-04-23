# !/usr/bin/python
# -*- coding: utf-8 -*-

import turtle
import random
import time

def publikum():

    #initialisering(oppstartsinformasjon).
    eksempel = turtle.Turtle()        #gi navn til instans.
    screen=turtle.Screen()            #gi navn til visningsflaten (vindu)
    screen.setup(1000,400)             #skjermstorrelse
    screen.bgcolor('black')        #skjermbakgrunn
    
    #bakgrunnsbilde
    #bilde = './turtlelpg.png'
    #screen.bgpic(bilde)
    #screen.update()
    
    
    #initialisering av pen og figur.
    eksempel.penup()            #Pen up, skriver ikke til skjerm.
    eksempel.ht()                #Figur hidden.
    eksempel.pensize(4)
    eksempel.speed(1)
    eksempel.shape('turtle')    #Figur som vises.
    eksempel.pencolor('black')    #Pen farge.
    skriftStr = 40                #Variabel med skriftsize.

    eksempel.setpos (-380, 0)
    eksempel.pendown()
    eksempel.write('Velkommen til Mittskogtangen sjokolade og is. ', font=("Arial", skriftStr, "bold")) # konfigurerer font
    time.sleep(4)
    eksempel.penup()
    eksempel.clear()
    #turtle.colormode(255)
    
    eksempel.setpos (-300, 100)
    eksempel.pendown()
    eksempel.write('Vi selger. ', font=("Arial", skriftStr, "bold")) # konfigurerer font
    eksempel.penup()
    time.sleep(2)
    
    eksempel.setpos (-250, 50)
    eksempel.pendown()
    eksempel.write('sjokolade. ', font=("Arial", skriftStr, "bold")) 
    eksempel.penup()
    time.sleep(2)
    
    eksempel.setpos (-200, 0)
    eksempel.pendown()
    eksempel.write('softis. ', font=("Arial", skriftStr, "bold")) 
    eksempel.penup()
    time.sleep(2)
    
    eksempel.setpos (-150, -50)
    eksempel.pendown()
    eksempel.write('youghurtis. ', font=("Arial", skriftStr, "bold")) 
    eksempel.penup()
    time.sleep(4)
    eksempel.clear()
    
    eksempel.pencolor('red')    #Pen farge.
    
    eksempel.setpos (-480, -0)
    eksempel.pendown()
    eksempel.write('Grunnet kommandoen "screen.mainloop" blir vindu stående. ', font=("Arial", skriftStr, "bold")) 
    eksempel.penup()
    time.sleep(4)
    eksempel.clear()

    screen.mainloop()
    
publikum()    