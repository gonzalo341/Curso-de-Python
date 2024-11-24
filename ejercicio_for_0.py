#triangulo usando la libreria de turtle
import turtle

pantalla = turtle.Screen()
pantalla.title("Dibujar una linea recta")
pantalla.bgcolor("green")

tortuga = turtle.Turtle()
tortuga.color("blue")
tortuga.pensize(3)

tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)
tortuga.left(135)
tortuga.forward(140)
tortuga.left(140)

pantalla.mainloop()