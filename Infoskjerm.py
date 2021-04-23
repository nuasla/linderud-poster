import turtle
import math
import random
import time
# -*- coding: utf-8 -*-

def main():
    #initialisering av pen og figur.
    tekst=turtle.Turtle() #gir navn til instans.
    tekst.penup()            #pen up, skriver ikke til skjerm.
    tekst.ht()                #figur hidden. viser ikke den lille dotten
    tekst.pensize(5)
    tekst.speed(-1)
    tekst.shape('turtle')    #figur som vises.
    tekst.pencolor('white')    #pen farge.
    skriftStr = 41                #variabel med skriftsize.

    #initialisering(oppstartsinformasjon).
    screen=turtle.Screen()            #gir navn til visningsflaten (vindu)
    screen.bgcolor('black')        #skjermbakgrunn
    screen.setup(1355,700)  #skjermstorrelse


    time.sleep(2) #tiden før logo popper opp til skjerm
    turtle.bgpic("logo-lpg-gr_800x600.png") #printer logo. butikken kan bytte bilde,ettersom hvordan de vil ha det.
    tekst.setpos (-300, 100)
    time.sleep(2)
    turtle.bgpic("nopic") #Fjerner logo

    tekst.setpos (-300, 100)
    tekst.pendown()
    tekst.write('''VELKOMMEN TIL\nLINDERUD PIZZA OG\nGRILL''', font=("Arial", skriftStr, "bold")) # konfigurerer font
    time.sleep(3)
    tekst.penup()
    tekst.clear()
    turtle.colormode(255)

    tekst.setpos (-300, 100)
    tekst.pendown()
    tekst.write('SJEKK VÅR MENY OG BESTILL', font=("Arial", skriftStr, "bold")) # konfigurerer font
    tekst.penup()
    time.sleep(3)
    tekst.clear()

    tekst.setpos (-250, 100)
    tekst.pendown()
    tekst.write('VI SELGER BLANT ANNET', font=("Arial", skriftStr, "bold")) # konfigurerer font
    tekst.penup()
    time.sleep(2)
    tekst.clear()

    tekst.pencolor('white') #printer teksten i 'brun' farge
    tekst.setpos (-250, 50)
    tekst.pendown()
    tekst.write('PIZZA', font=("Arial", skriftStr, "bold")) 
    tekst.penup()
    time.sleep(1)

    tekst.pencolor('red') #printer teksten i 'rod' farge
    tekst.setpos (-200, 0)
    tekst.pendown()
    tekst.write('KEBAB', font=("Arial", skriftStr, "bold")) 
    tekst.penup()
    time.sleep(1)

    tekst.pencolor('green') #printer teksten i 'gronn' farge
    tekst.setpos (-150, -50)
    tekst.pendown()
    tekst.write('BURGERE', font=("Arial", skriftStr, "bold")) 
    tekst.penup()
    time.sleep(3)
    tekst.clear()

    tekst.pencolor('orange') #printer teksten i 'oransje' farge
    tekst.setpos (-300, 0)
    tekst.pendown()
    turtle.bgpic('./kebab.png')
    turtle.update()
    tekst.write('''KEBAB TIL KUN 65kr\nMEDIUM 75kr\nSTOR 95kr''', font=("Arial", skriftStr, "bold")) 
    tekst.penup()
    time.sleep(6)
    tekst.clear()
    turtle.bgpic("nopic") #Fjerner bilde
    

    tekst.pencolor('yellow') #printer teksten i 'gul' farge
    tekst.setpos (-500, 100)
    tekst.pendown()
    tekst.write('TILBUD!\nCheeseburger 100g til kun 55kr', font=("Arial", skriftStr, "bold")) 
    tekst.penup()
    time.sleep(5)
    tekst.clear()

    tekst.pencolor('white') #printer teksten i 'hvit' farge
    tekst.setpos (-350, -0)
    tekst.pendown()
    tekst.write('HAR DU HUSKET DRIKKE TIL MATEN?', font=("Arial", skriftStr, "bold")) 
    tekst.penup()
    time.sleep(3)
    tekst.clear()

    tekst.pencolor('green') #printer teksten i 'gronn' farge
    tekst.setpos (-480, -0)
    tekst.pendown()
    tekst.write('DRIKKE TIL MAT 28kr', font=("Arial", skriftStr, "bold")) 
    tekst.penup()
    time.sleep(5)
    tekst.clear()

    tekst.pencolor('orange')
    tekst.setpos (-350, 0)
    tekst.pendown()
    tekst.write('VÅRE POPULÆRE RETTER', font=("Arial", skriftStr, "bold"))    
    tekst.penup()
    time.sleep(2)
    tekst.clear()
    
    

    main()
main()

    
    #screen.mainloop() #Grunnet 'screen.mainloop()' vil skjermen stå oppe.
#Kjører i rekkefølge etter sirkelene:
#logo_visning()

    #publikum()


#publikum()

#tekst.pencolor('white')    #Kode Pen farge.



