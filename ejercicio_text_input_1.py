import turtle
import time
import random

# Configuración de la pantalla
pantalla = turtle.Screen()
pantalla.title("Snake")
pantalla.bgcolor("orange")
pantalla.setup(width=600, height=600)
pantalla.tracer(0)

# Solicitar el nombre del jugador
nombre_jugador = pantalla.textinput("Nombre del Jugador", "Ingresa tu nombre:")
if not nombre_jugador:
    nombre_jugador = "Anónimo"

# Elegir el color de la serpiente
colores_disponibles = ["darkgreen", "blue", "red", "purple", "orange", "yellow"]
color_serpiente = None

while color_serpiente not in colores_disponibles:
    seleccion_color = pantalla.textinput(
        "Selección de color",
        f"Elige el color de tu serpiente:\n{' - '.join(colores_disponibles)}",
    )
    if seleccion_color:
        seleccion_color = seleccion_color.lower()
        if seleccion_color in colores_disponibles:
            color_serpiente = seleccion_color
    else:
        color_serpiente = "darkgreen"

# Dibujar el borde del juego
linea_limite = turtle.Turtle()
linea_limite.speed(0)
linea_limite.color("white")
linea_limite.penup()
linea_limite.goto(-250, -250)
linea_limite.pendown()
linea_limite.pensize(10)
for _ in range(4):
    linea_limite.forward(500)
    linea_limite.left(90)
linea_limite.hideturtle()

# Cabeza de la serpiente
serpiente = turtle.Turtle()
serpiente.speed(0)
serpiente.shape("square")
serpiente.color(color_serpiente)
serpiente.penup()
serpiente.goto(0, 0)
serpiente.direction = "stop"

# Segmentos de la serpiente
segmentos = []

# Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(random.randint(-230, 230), random.randint(-230, 230))

# Puntaje y nivel
puntaje = 0
puntaje_maximo = 0
nivel = 1
velocidad = 0.1

# Texto del puntaje
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write(
    f"Jugador: {nombre_jugador} Puntaje: {puntaje}  Puntaje más alto: {puntaje_maximo}    Nivel: {nivel}",
    align="center",
    font=("Arial", 12, "bold"),
)

def actualizar_puntaje():
    texto.clear()
    texto.write(
        f"Jugador: {nombre_jugador} Puntaje: {puntaje}  Puntaje más alto: {puntaje_maximo}    Nivel: {nivel}",
        align="center",
        font=("Arial", 12, "bold"),
    )

# Mostrar "Game Over"
def game_over():
    serpiente.direction = "stop"
    comida.hideturtle()
    for segmento in segmentos:
        segmento.hideturtle()
    segmentos.clear()
    texto.goto(0, 0)
    texto.write("GAME OVER\nPresiona 'r' para reiniciar", align="center", font=("Arial", 24, "bold"))

# Reiniciar el juego
def reiniciar_juego():
    global puntaje, nivel, velocidad
    comida.showturtle()
    serpiente.goto(0, 0)
    serpiente.direction = "stop"
    for segmento in segmentos:
        segmento.hideturtle()
    segmentos.clear()
    comida.goto(random.randint(-230, 230), random.randint(-230, 230))
    texto.clear()
    puntaje = 0
    nivel = 1
    velocidad = 0.1
    actualizar_puntaje()

# Movimiento de la serpiente
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

# Control de dirección
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
pantalla.onkeypress(arriba, "Up")
pantalla.onkeypress(abajo, "Down")
pantalla.onkeypress(izquierda, "Left")
pantalla.onkeypress(derecha, "Right")
pantalla.onkeypress(reiniciar_juego, "r")

# Bucle principal
while True:
    pantalla.update()

    # Verificar si la serpiente choca con el borde
    if abs(serpiente.xcor()) > 240 or abs(serpiente.ycor()) > 240:
        game_over()

    # Verificar si la serpiente come la comida
    if serpiente.distance(comida) < 20:
        comida.goto(random.randint(-230, 230), random.randint(-230, 230))
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color(color_serpiente)
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)
        puntaje += 10
        actualizar_puntaje()

    # Mover el cuerpo de la serpiente
    for i in range(len(segmentos) - 1, 0, -1):
        x = segmentos[i - 1].xcor()
        y = segmentos[i - 1].ycor()
        segmentos[i].goto(x, y)
    if len(segmentos) > 0:
        x = serpiente.xcor()
        y = serpiente.ycor()
        segmentos[0].goto(x, y)

    mover()

    # Verificar si la serpiente choca consigo misma
    for segmento in segmentos:
        if segmento.distance(serpiente) < 20:
            game_over()

    time.sleep(velocidad)
