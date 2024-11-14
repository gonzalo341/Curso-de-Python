#Contorno de la estrella
import turtle

pantalla = turtle.Screen()
pantalla.title("Dibujar una linea recta")
pantalla.bgcolor("green")

tortuga = turtle.Turtle()
tortuga.color("blue")
tortuga.begin_fill()
tortuga.pensize(3)

for triangulos in range(5):
    tortuga.left(-70)
    tortuga.forward(-100)
    tortuga.left(-218)
    tortuga.forward(-100)

#tortuga.end_fill()

pantalla.mainloop()