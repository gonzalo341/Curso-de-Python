#Cuadro de Texto
import turtle
import time
import random

pantalla = turtle.Screen()
pantalla.title("Dibujar una linea recta")
pantalla.bgcolor("green")
pantalla.setup(width=600,height=600)
pantalla.tracer(0)

# Solicitar el nombre del jugador
nombre_jugador = pantalla.textinput("Nombre del Jugador", "Ingresa tu nombre:")
if not nombre_jugador:
   nombre_jugador = "Anonimo"

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
linea_limite.color("white")
linea_limite.penup()
linea_limite.goto(-250,-250)
linea_limite.pendown()
linea_limite.pensize(10)

for _ in range (4):
    linea_limite.forward(500)
    linea_limite.left(90)

linea_limite.hideturtle()

#cabeza_de_la_serpiente
serpiente = turtle.Turtle()
serpiente.speed(0)
serpiente.shape("square")
serpiente.pencolor(color_serpiente)
serpiente.penup()
serpiente.goto(0,0)
serpiente.direction = "stop"

segmentos = []

#comida para la serpiente
comida = turtle.Turtle()
comida.speed(0)
comida.shape("turtle")
comida.pencolor("darkgreen")
comida.penup()
x = random.randint(-230,230)
y = random.randint(-230,230)
comida.goto(x,y)

#puntaje
puntaje = 0
puntaje_maximo = 0
nivel = 1
velocidad = 0.1

# Mostrar el puntaje y nombre del jugador
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write(f"Jugador: {nombre_jugador} Puntaje: {puntaje}  Puntaje mas alto: {puntaje_maximo}    Nivel: {nivel}", align= "center", font =("Arial", 12, "normal"))

def actualizar_puntaje():
    texto.clear()
    texto.write(f"Jugador: {nombre_jugador} Puntaje: {puntaje}  Puntaje mas alto: {puntaje_maximo}    Nivel: {nivel}", align= "center", font =("Arial", 12, "normal"))

def game_over():
    serpiente.hideturtle()
    comida.hideturtle()
    gameOver = turtle.Turtle()
    gameOver.speed(0)
    gameOver.color("white")
    gameOver.penup()
    gameOver.hideturtle()
    gameOver.goto(0,0)
    gameOver.write(f"GAME OVER", align= "center", font =("Arial", 42, "bold"))
    time.sleep(0.5)

def reiniciar_juego():

    game_over()

    global puntaje, puntaje_maximo, nivel, velocidad
    serpiente.goto(0,0)
    serpiente.direction = "stop"

    #Ocultar los segmentos
    for i in segmentos:
        i.goto(1000,1000)

    #Limpiar la lista de segmentos
    segmentos.clear()

    #Resetear puntaje y niveles
    if puntaje > puntaje_maximo:
        puntaje_maximo = puntaje
    puntaje = 0
    nivel = 1
    velocidad = 0.1

#nuevo segmento de la serpiente
for i in range (50):
    nuevo_segmento = turtle.Turtle()
    nuevo_segmento.speed(0)
    nuevo_segmento.shape("circle")
    nuevo_segmento.pencolor(color_serpiente)
    nuevo_segmento.penup()
    nuevo_segmento.goto(0,0) #goto(-20 * (i+1),0)
    segmentos.append(nuevo_segmento)

#definir el movimiento de la serpiente
def mover():
    if serpiente.direction == "up":
        y = serpiente.ycor()
        serpiente.sety(y+20)
    if serpiente.direction == "down":
        y = serpiente.ycor()
        serpiente.sety(y-20)
    if serpiente.direction == "left":
        x = serpiente.xcor()
        serpiente.setx(x-20)
    if serpiente.direction == "right":
        x = serpiente.xcor()
        serpiente.setx(x+20)

    # Envoltura de los bordes
    if serpiente.xcor() > 240:
        serpiente.setx(-240)
    elif serpiente.xcor() < -240:
        serpiente.setx(240)
    if serpiente.ycor() > 240:
        serpiente.sety(-240)
    elif serpiente.ycor() < -240:
        serpiente.sety(240) 

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

while True:
    pantalla.update()

    mover()

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
    
        while True:
            x = random.randint(-230,230)
            y = random.randint(-230,230)
            nueva_posicion = (x,y)
            distancia_serpiente = serpiente.distance(nueva_posicion)
            distancia_segmentos = all(segmento.distance(nueva_posicion) > 20 for segmento in segmentos)
            if distancia_serpiente > 20 and distancia_segmentos:
                comida.goto(x,y)
                break
        
        #Aumentar puntaje
        puntaje += 10
        actualizar_puntaje()

        #Aumentar nivel cada 50 puntos
        if puntaje > 50:
            nivel += 1
            velocidad *= 0.9
            actualizar_puntaje()
    
    #mover los segmentos en orden inverso
    for i in range(len(segmentos)-1, 0, -1):
        x = segmentos[i - 1].xcor()
        y = segmentos[i - 1].ycor()
        segmentos[i].goto(x,y)
    
    #Mover el primer segmento
    if len(segmentos) > 0:
        x = ultima_posicion[0]
        y = ultima_posicion[1]
        segmentos[0].goto(x,y)
    
    #for segmento in segmentos:
    #    if segmento.distance(serpiente)< 10:
    #        reiniciar_juego()
    #        break
    
    time.sleep(velocidad)