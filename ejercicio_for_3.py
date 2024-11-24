#Contorno de la estrella
import turtle

pantalla = turtle.Screen()
pantalla.title("Estrella usando for")
pantalla.bgcolor("darkblue")

tortuga = turtle.Turtle()
tortuga.color("ghostwhite")
tortuga.begin_fill()
tortuga.pensize(4)

for triangulos in range(5):
    tortuga.left(-70)
    tortuga.forward(-100)
    tortuga.left(-218)
    tortuga.forward(-100)

tortuga.end_fill()

pantalla.mainloop()