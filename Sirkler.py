import turtle
import math
import random
import time


screen = turtle.Screen()
screen.bgcolor('black')
screen.setup(1350,700)

Gronn_sirkel = turtle.Turtle()
Gronn_sirkel.speed(50)
Gronn_sirkel.color('green')
rotate=int(360)



def LageSirkler(t,size):
    for i in range(10):
        t.circle(size)
        size=size-15
def ForskjelligeSirkler(t,size,repeat):
  for i in range (repeat):
    LageSirkler(t,size)
    t.right(360/repeat)

ForskjelligeSirkler(Gronn_sirkel,120,10)

#GulSirkel = turtle.Turtle()
#GulSirkel.speed(1200)
#GulSirkel.color('yellow')
#rotate=int(360)
#ForskjelligeSirkler(GulSirkel,110,10)

#Rød_sirkel = turtle.Turtle()
#Rød_sirkel.speed(1200)
#Rød_sirkel.color('red')
#rotate=int(360)
#ForskjelligeSirkler(Rød_sirkel,100,10)

def clear():
    Gronn_sirkel.clear()
    #Rød_sirkel.clear()
    #GulSirkel.clear()
    
#def logo_visning():
	#initialisering, oppstartsinfo
	#logo = turtle.Screen()
	#logo.setup(600,400)
	#logo.bgpic('logo-lpg-gr.png')
    ##logo.update()
    ##time.sleep(3)
    ##logo.size(10)
	##logo.update()
 
#def show_text():
    #Velkomst=turtle.Turtle()
    #Velkomst.setpos (-190, 0)
    #Velkomst.color ('red')
    #Velkomst.pendown()
    #Velkomst.speed(1)
    #Velkomst.write(,
    #font=("Roboto", 36, "bold")) # konfigurerer font
    #Velkomst.sleep(5)
    #Velkomst.penup()
    #Velkomst.clear()
    
def publikum():

    #initialisering(oppstartsinformasjon).
    tekst = turtle.Turtle()        #gi navn til instans.
    screen=turtle.Screen()            #gi navn til visningsflaten (vindu)
    screen.setup(1400,700)             #skjermstorrelse
    screen.bgcolor('black')        #skjermbakgrunn
    
    #bakgrunnsbilde
    #bilde = './turtlelpg.png'
    #screen.bgpic(bilde)
    #screen.update()
    
    
    #initialisering av pen og figur.
    tekst.penup()            #Pen up, skriver ikke til skjerm.
    tekst.ht()                #Figur hidden.
    tekst.pensize(5)
    tekst.speed(1)
    tekst.shape('turtle')    #Figur som vises.
    tekst.pencolor('white')    #Pen farge.
    skriftStr = 40                #Variabel med skriftsize.

    tekst.setpos (-380, 0)
    tekst.pendown()
    tekst.write('''VELKOMMEN TIL\nLINDERUD PIZZA OG\nGRILL''', font=("Arial", skriftStr, "bold")) # konfigurerer font
    time.sleep(4)
    tekst.penup()
    tekst.clear()
    turtle.colormode(255)
    
    tekst.setpos (-300, 100)
    tekst.pendown()
    tekst.write('Vi selger blant annet', font=("Arial", skriftStr, "bold")) # konfigurerer font
    tekst.penup()
    time.sleep(3)
    tekst.clear()
    
    tekst.setpos (-250, 50)
    tekst.pendown()
    tekst.write('''Kebab til kun 65kr.\nVelg mellom liten,\nmedium og stor størrelse\nfor kun 10/20kr ekstra''', font=("Arial", skriftStr, "bold")) 
    tekst.penup()
    time.sleep(7)
    tekst.clear()
    
    tekst.setpos (-500, 100)
    tekst.pendown()
    tekst.write('Tilbud!\nCheeseburger 100g til kun 55kr', font=("Arial", skriftStr, "bold")) 
    tekst.penup()
    time.sleep(5)
    tekst.clear()
    
    tekst.setpos (-150, -50)
    tekst.pendown()
    tekst.write('Har du husket drikke til maten?', font=("Arial", skriftStr, "bold")) 
    tekst.penup()
    time.sleep(4)
    tekst.clear()
    
    tekst.pencolor('white')    #Pen farge.
    tekst.setpos (-480, -0)
    tekst.pendown()
    tekst.write('Drikke til maten 28kr', font=("Arial", skriftStr, "bold")) 
    tekst.penup()
    time.sleep(5)
    tekst.clear()

    
    #screen.mainloop()
#Kjører i rekkefølge etter sirkelene:
clear()
#logo_visning()
publikum()






