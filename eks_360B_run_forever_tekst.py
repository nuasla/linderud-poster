import turtle
import time

#Endre bakgrunnsbilde.
#Et bilde i 6 sek. Bildeskift. Nytt bilde i 10 sek.
# !/usr/bin/python
# -*- coding: utf-8 -*-

def bildeskift():

	#initialisering, oppstartsinfo
	eksempel = turtle.Screen()
	eksempel.setup(600,400)
	eksempel.bgpic('./bilder/sommer_mittskogtangen_800x600.png')
	eksempel.update()

	#endre bakgrunnsbilde. Viser startbilde i 6 sekunder, deretter nytt bilde.
	time.sleep(6)
	eksempel.bgpic('./bilder/sommer_kajakk_800x600.png')
	eksempel.update()

	#endre bakgrunnsbilde. Viser startbilde i 6 sekunder, deretter nytt bilde.
	time.sleep(6)
	eksempel.bgpic('./bilder/sommer_natur_800x600.png')
	eksempel.update()
	time.sleep(6)
	
	test = = turtle.Turtle()
	test.penup()            #Pen up, skriver ikke til skjerm.
    #test.ht()                #Figur hidden.
    test.pensize(4)
    test.speed(1)
    test.shape('turtle')    #Figur som vises.
    test.pencolor('black')    #Pen farge.
    skriftStr = 25                #Variabel med skriftsize.

    test.setpos (-380, 0)
    test.pendown()
    test.write('Velkommen til Linderud pizza og grill. ', font=("Arial", skriftStr, "bold")) # konfigurerer font
    time.sleep(4)
    test.penup()
    test.clear()
	
	bildeskift()
	
bildeskift()	
	