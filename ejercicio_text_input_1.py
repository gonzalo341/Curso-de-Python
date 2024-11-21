#Cuadro de Texto
import turtle
import time

pantalla = turtle.Screen()
pantalla.title("Dibujar una linea recta")
pantalla.bgcolor("green")
pantalla.listen()
pantalla.tracer()

nombre_de_usuario = pantalla.textinput(
    "Nombre del usuario",
    "Ingrese su nombre" 
)

if nombre_de_usuario == (""):
    jugador = "Anonimo"
"""
color_de_pantalla = pantalla.textinput(
    "color de pantalla",
    "white,black,red,green,blue,yellow,"
)

pantalla.bgcolor(color_de_pantalla)
"""
colores_disponibles = ["darkgreen", "blue", "red", "purple", "orange", "yellow"]
color_serpiente = None

while color_serpiente not in colores_disponibles:
    seleccion_color = pantalla.textinput("Selección de color",
                                         f"Elige el color de tu serpiente:\n{'-'.join(colores_disponibles)}")
    if seleccion_color:
        seleccion_color = seleccion_color.lower()
        if seleccion_color in colores_disponibles:
            color_serpiente = seleccion_color
        else: pantalla.textinput ("selección de color",
                                  f"Color invalido, Por favor, elige uno de los siguientes:\n{'-'.join(colores_disponibles)}")
    else: color_serpiente = "darkgreen"

linea_limite = turtle.Turtle()
linea_limite.speed(0)
linea_limite.teleport(-250,-250)
linea_limite.color("red")
linea_limite.pensize(10)

for limite_del_juego in range (4):
    linea_limite.forward(500)
    linea_limite.left(90)

linea_limite.hideturtle

#cabeza_de_la_serpiente
cabeza_de_la_serpiente = turtle.Turtle()
cabeza_de_la_serpiente.speed(0)
cabeza_de_la_serpiente.shape("square")
cabeza_de_la_serpiente.pencolor(color_serpiente)
cabeza_de_la_serpiente.penup()
cabeza_de_la_serpiente.goto(0,0)
cabeza_de_la_serpiente.direction = "stop"

cantidad_de_segmentos = 3
segmentos = []

#nuevo segmento de la serpiente
for i in range (cantidad_de_segmentos):
    nuevo_segmento = turtle.Turtle()
    nuevo_segmento.speed(0)
    nuevo_segmento.shape("circle")
    nuevo_segmento.pencolor(color_serpiente)
    nuevo_segmento.penup()
    nuevo_segmento.goto(20 * (i+1),0)
    segmentos.append(nuevo_segmento)


#cola de la serpiente
cola_de_la_serpiente = turtle.Turtle()
cola_de_la_serpiente.shape("triangle")
cola_de_la_serpiente.pencolor(color_serpiente)
cola_de_la_serpiente.penup()
cola_de_la_serpiente.goto(20 * (i+2),0)
cola_de_la_serpiente.speed(0)

segmentos.append(cola_de_la_serpiente)

#definir el movimiento de la serpiente
def mover():
    if cabeza_de_la_serpiente.direction == "up":
        y = cabeza_de_la_serpiente.ycor()
        cabeza_de_la_serpiente.sety(y + 20)
    if cabeza_de_la_serpiente.direction == "down":
        y = cabeza_de_la_serpiente.ycor()
        cabeza_de_la_serpiente.sety(y - 20)
    if cabeza_de_la_serpiente.direction == "left":
        x = cabeza_de_la_serpiente.xcor()
        cabeza_de_la_serpiente.setx(x - 20)
    if cabeza_de_la_serpiente.direction == "right":
        x = cabeza_de_la_serpiente.xcor()
        cabeza_de_la_serpiente.setx(x + 20)

for i in range(len(segmentos)-1,0,-1):
    x = segmentos[i-1].xcor()
    y = segmentos[i-1].ycor()
    segmentos[i].goto(x,y)

if len (segmentos) > 0:
    x = cabeza_de_la_serpiente.xcor()
    y = cabeza_de_la_serpiente.ycor()
    segmentos[i].goto(x,y)

def arriba():
    if cabeza_de_la_serpiente.direction != "down":
        cabeza_de_la_serpiente.direction = "up"

def abajo():
    if cabeza_de_la_serpiente.direction != "up":
        cabeza_de_la_serpiente.direction = "down"

def izquierda():
    if cabeza_de_la_serpiente.direction != "right":
        cabeza_de_la_serpiente.direction = "left"

def derecha():
    if cabeza_de_la_serpiente.direction != "left":
        cabeza_de_la_serpiente.direction = "right"

pantalla.listen()
pantalla.onkeypress(arriba,"Up")
pantalla.onkeypress(abajo,"Down")
pantalla.onkeypress(izquierda,"Left")
pantalla.onkeypress(derecha,"Right")

while True:
    pantalla.update()

    mover()

    time.sleep(0.1)
