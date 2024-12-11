#Cuadrado con for
import turtle

pantalla = turtle.Screen()
pantalla.title("Cuadrado con for")
pantalla.bgcolor("green")

tortuga = turtle.Turtle()
tortuga.color("blue")
tortuga.begin_fill()
tortuga.pensize(3)

for cuadrado in range(4):
 tortuga.forward(100)
 tortuga.left(90)

#tortuga.end_fill()

pantalla.mainloop()