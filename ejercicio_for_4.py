#Estrella (sin terminar)
import turtle

pantalla = turtle.Screen()
pantalla.title("Triangulo usando for")
pantalla.bgcolor("green")

tortuga = turtle.Turtle()
tortuga.color("blue")
tortuga.begin_fill()
tortuga.pensize(3)

for triangulos in range(3):
    tortuga.forward(200)
    tortuga.right(70)

#tortuga.end_fill()

pantalla.mainloop()