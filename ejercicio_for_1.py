#Triangulo con for
import turtle

pantalla = turtle.Screen()
pantalla.title("Triangulo con for")
pantalla.bgcolor("green")

tortuga = turtle.Turtle()
tortuga.color("blue")
tortuga.begin_fill()
tortuga.pensize(3)

for triangulo in range(3):
 tortuga.forward(100)
 tortuga.left(120)

#tortuga.end_fill()

pantalla.mainloop()