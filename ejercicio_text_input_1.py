#Cuadro de Texto
import turtle
import time
import random

pantalla = turtle.Screen()
pantalla.title("Dibujar una linea recta")
pantalla.bgcolor("green")
pantalla.setup(width=600,height=600)
pantalla.tracer(0)

nombre_de_usuario = pantalla.textinput(
    "Nombre del usuario",
    "Ingrese su nombre" 
)

if nombre_de_usuario == (""):
    jugador = "Anonimo"

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
linea_limite.goto(-250,-250)
linea_limite.color("red")
linea_limite.pendown()
linea_limite.pensize(10)

for _ in range (4):
    linea_limite.forward(500)
    linea_limite.left(90)

linea_limite.hideturtle()
segmentos = []

#cabeza_de_la_serpiente
serpiente = turtle.Turtle()
serpiente.speed(0)
serpiente.shape("square")
serpiente.pencolor(color_serpiente)
serpiente.penup()
serpiente.goto(0,0)
serpiente.direction = "stop"
segmentos.append(serpiente)

#puntaje
puntaje = 0
puntaje_maximo = 0
nivel = 1
velocidad = 0.1

texto = turtle.Turtle()
texto.speed(0)
texto.color("black")
texto.penup()
texto.hideturtle()
texto.goto(-240,260)
texto.write(f"Jugador: {nombre_de_usuario} Puntaje: {puntaje} Puntaje Maximo: {puntaje_maximo}")

def actualizar_puntaje():
    texto.clear
    texto.write(f"Jugador: {nombre_de_usuario} Puntaje: {puntaje} Puntaje Maximo: {puntaje_maximo}")

#nuevo segmento de la serpiente
for i in range (3):
    nuevo_segmento = turtle.Turtle()
    nuevo_segmento.speed(0)
    nuevo_segmento.shape("circle")
    nuevo_segmento.pencolor(color_serpiente)
    nuevo_segmento.penup()
    nuevo_segmento.goto(-20 * (i+1),0)
    segmentos.append(nuevo_segmento)

def arriba():
    if serpiente.direction != "down":
        serpiente.direction = "up"

def abajo():
    if serpiente.direction != "up":
        serpiente.direction = "down"

def izquierda():
    if serpiente.direction != "right":
        serpiente.direction = "left"

def derecha():
    if serpiente.direction != "left":
        serpiente.direction = "right"

pantalla.listen()
pantalla.onkeypress(arriba,"Up")
pantalla.onkeypress(abajo,"Down")
pantalla.onkeypress(izquierda,"Left")
pantalla.onkeypress(derecha,"Right")

#comida para la serpiente
comida = turtle.Turtle()
comida.shape("turtle")
comida.pencolor("red")
comida.penup()
comida.goto(-20,-20)
comida.speed(0)

while True:
    pantalla.update()

    time.sleep(0.1)

    ultima_posicion = serpiente.position()

    if serpiente.distance(comida) < 20:
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("circle")
        nuevo_segmento.pencolor(color_serpiente)
        nuevo_segmento.penup()
    
    if len(segmentos) > 0:
        ultimo_segmento = segmentos[-1]
        nuevo_segmento.goto(ultimo_segmento.position())
    else:
        nuevo_segmento.goto(ultima_posicion)
    
    segmentos.append(nuevo_segmento)
    #definir el movimiento de la serpiente
    def mover():
        if serpiente.direction == "up":
            y = serpiente.ycor()
            serpiente.sety(y + 20)
    
        if serpiente.direction == "down":
            y = serpiente.ycor()
            serpiente.sety(y - 20)
    
        if serpiente.direction == "left":
            x = serpiente.xcor()
            serpiente.setx(x - 20)
    
        if serpiente.direction == "right":
            x = serpiente.xcor()
            serpiente.setx(x + 20)
    
        for i in range(len(segmentos)-1,0,-1):
            x = segmentos[i-1].xcor()
            y = segmentos[i-1].ycor()
            segmentos[i].goto(x,y)
    
        if len (segmentos) > 0:
            x = serpiente.xcor()
            y = serpiente.ycor()
            segmentos[0].goto(x,y)

    mover()
    
    x = random.randint(-230,230)
    y = random.randint(-230,230)
    nueva_posicion = (x,y)
    
    puntaje += 10
    actualizar_puntaje()

    if puntaje % 50 == 0:
        nivel += 1
        velocidad *= 0.9
        actualizar_puntaje()