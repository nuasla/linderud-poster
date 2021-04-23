import turtle
import time

#Endre bakgrunnsbilde.
#Et bilde i 6 sek. Bildeskift. Nytt bilde i 10 sek.

#initialisering, oppstartsinfo
eksempel = turtle.Screen()
eksempel.setup(600,400)
eksempel.bgpic('./kebab.png')
eksempel.update()

#endre bakgrunnsbilde. Viser startbilde i 6 sekunder, deretter nytt bilde.
time.sleep(6)
eksempel.bgpic('./cola.png')
eksempel.update()

#endre bakgrunnsbilde. Viser startbilde i 6 sekunder, deretter nytt bilde.
time.sleep(6)
eksempel.bgpic('./munnbind.png')
eksempel.update()
time.sleep(10)