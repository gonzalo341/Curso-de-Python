#juego de la serpiente

#librerias importadas
import turtle
import time

pantalla = turtle.Screen()
pantalla.title("Juego de la serpiente")
pantalla.bgcolor("green")

nombre_de_usuario = pantalla.textinput(
    "Nombre del usuario",
    "Ingrese su nombre" 
) 
if nombre_de_usuario == (""):
    jugador = "Anonimo"

colores_disponibles = ["darkgreen", "blue", "red", "purple", "orange", "yellow"]
color_serpiente = None

#.strip() = borra los espacios del inicio y del final del prompt ingresado
#.lower() = pasa todas las mayusculas a minusculas del prompt ingresado
#\n = salto de linea
#''.join() = signo que separa las lista

def elegir_color():
    while True:
        color_serpiente = pantalla.textinput("Selección de color", f"Elige el color de tu serpiente:\n{' - '.join(colores_disponibles)}")
        if color_serpiente is None or color_serpiente.strip() == "": #Si no se selecciona un color se asignara el color por defecto
            pantalla.textinput("Selección de color", "No se seleccionó un color. Se asignó 'darkgreen' por defecto.")
            return "darkgreen"
        color_serpiente = color_serpiente.strip().lower()
        if color_serpiente in colores_disponibles: #Si se selecciona un color valido entonces termina el while
            return color_serpiente
        else:
            while True: #si ingresa un color invalido entonces aparecera el cartel de color invalido hasta que se eliga un color valido o se asigne el color por defecto
                color_serpiente = pantalla.textinput("Selección de color", f"Color inválido. Por favor, elige uno de los siguientes:\n{' - '.join(colores_disponibles)}")
                if color_serpiente is None or color_serpiente.strip() == "":
                    pantalla.textinput("Selección de color", "No se seleccionó un color. Se asignó 'darkgreen' por defecto.")
                    return "darkgreen"
                color_serpiente = color_serpiente.strip().lower()
                if color_serpiente in colores_disponibles:
                    return color_serpiente

color_serpiente = elegir_color()

#limites del juego
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

def arriba(): #si se mueve hacia arriba no se puede mover hacia abajo
    if cabeza_de_la_serpiente.direction != "down":
        cabeza_de_la_serpiente.direction = "up"

def abajo(): #si se mueve hacia abajo no se puede mover hacia arriba
    if cabeza_de_la_serpiente.direction != "up":
        cabeza_de_la_serpiente.direction = "down"

def izquierda(): #si se mueve hacia derecha no se puede mover hacia la derecha
    if cabeza_de_la_serpiente.direction != "right":
        cabeza_de_la_serpiente.direction = "left"

def derecha(): #si se mueve hacia derecha no se puede mover hacia la izquierda
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