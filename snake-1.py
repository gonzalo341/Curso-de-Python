#Cuadro de Texto
import turtle
import time
import random

pantalla = turtle.Screen()
pantalla.title("Snake")
pantalla.bgcolor("green")
pantalla.setup(width=600,height=600)
pantalla.tracer(0) # Desactiva la actualizacion de pantalla

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

# Dibujar el Borde del juego en color blanco
linea_limite = turtle.Turtle()
linea_limite.speed(0)
linea_limite.color("white")
linea_limite.penup()
linea_limite.goto(-250,-250)
linea_limite.pendown()
linea_limite.pensize(10)

# Dibuja el limite del juego de 500 x 500
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

segmentos = [] # Segmentos de la serpiente guardados

# Valor inicial del Puntaje, Puntaje Maximo, Nivel y Velocidad.
puntaje = 0
puntaje_maximo = 0
nivel = 1
velocidad = 0.1

#comida para la serpiente
comida = turtle.Turtle()
comida.speed(0)
comida.shape("turtle")
comida.pencolor("darkgreen")
comida.penup()

# Elegir una posicion inicial random 
x = random.randint(-230,230)
y = random.randint(-230,230)
comida.goto(x,y) # Envia la comida a la posicion elegida

# Mostrar el puntaje y nombre del jugador
texto = turtle.Turtle()
texto.speed(0)
texto.pencolor("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write(f"Jugador: {nombre_jugador} Puntaje: {puntaje}  Puntaje mas alto: {puntaje_maximo}    Nivel: {nivel}", align= "center", font =("Arial", 12, "bold"))

# Borrar el texto del puntaje y actualizarlo por el nuevo puntaje
def actualizar_puntaje():
    texto.clear()
    texto.write(f"Jugador: {nombre_jugador} Puntaje: {puntaje}  Puntaje mas alto: {puntaje_maximo}    Nivel: {nivel}", align= "center", font =("Arial", 12, "normal"))

# Nuevo segmento de la serpiente
for i in range (0):
    nuevo_segmento = turtle.Turtle()
    nuevo_segmento.speed(0)
    nuevo_segmento.shape("circle")
    nuevo_segmento.pencolor(color_serpiente)
    nuevo_segmento.penup()
    nuevo_segmento.goto(0,0) #goto(-20 * (i+1),0)
    segmentos.append(nuevo_segmento)

#definir el movimiento de la serpiente
def mover():
    # Mover 20 px hacia Arriba
    if serpiente.direction == "up":
        y = serpiente.ycor()
        serpiente.sety(y + 20)
    # Mover 20 px hacia Abajo
    if serpiente.direction == "down":
        y = serpiente.ycor()
        serpiente.sety(y - 20)
    # Mover 20 px hacia la Izquierda
    if serpiente.direction == "left":
        x = serpiente.xcor()
        serpiente.setx(x - 20)
    # Mover 20 px hacia Derecha
    if serpiente.direction == "right":
        x = serpiente.xcor()
        serpiente.setx(x + 20)

    # Envoltura de los bordes
    if serpiente.xcor() > 240:
        serpiente.setx(-240)
    elif serpiente.xcor() < -240:
        serpiente.setx(240)
    if serpiente.ycor() > 240:
        serpiente.sety(-240)
    elif serpiente.ycor() < -240:
        serpiente.sety(240) 

# Texto de Game Over que aparece al reiniciar el juego
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
    time.sleep(2)
    gameOver.hideturtle()
    serpiente.showturtle()
    comida.showturtle()

# Reiniciar el juego al colisionar
def reiniciar_juego():

    game_over()

    global puntaje, puntaje_maximo, nivel, velocidad
    time.sleep(1)
    serpiente.goto(0,0)
    serpiente.direction = "stop"

    # Ocultar los segmentos
    for segmento in segmentos:
        segmento.goto(1000,1000)

    # Limpiar la lista de segmentos agregados
    segmentos.clear()

    # Reiniciar puntaje, Nivel y velocidad
    if puntaje > puntaje_maximo:
        puntaje_maximo = puntaje
    puntaje = 0
    nivel = 1
    velocidad = 0.1
    actualizar_puntaje()

# Funciones para que no gire directamente y colisione con los segmentos
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

# Asignar las teclas de los controles
pantalla.listen()
pantalla.onkeypress(arriba,"Up")
pantalla.onkeypress(abajo,"Down")
pantalla.onkeypress(izquierda,"Left")
pantalla.onkeypress(derecha,"Right")

# Bucle principal
while True:
    pantalla.update()

    ultima_posicion = serpiente.position()

    mover()

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
    
        # Mover la comida a una posicion random
        while True:
            x = random.randint(-230,230)
            y = random.randint(-230,230)
            nueva_posicion = (x,y)
            distancia_serpiente = serpiente.distance(nueva_posicion)
            distancia_segmentos = all(segmento.distance(nueva_posicion) > 20 for segmento in segmentos)
            if distancia_serpiente > 20 and distancia_segmentos:
                comida.goto(x,y)
                break
        
        # Aumentar puntaje en 10 puntos
        puntaje += 10
        actualizar_puntaje()

        # Aumentar el nivel y la velocidad cada 50 puntos
        if puntaje > 50:
            nivel += 1
            velocidad *= 0.9
            actualizar_puntaje()
    
    # Mover los segmentos en orden inverso
    for i in range(len(segmentos)-1, 0, -1):
        x = segmentos[i - 1].xcor()
        y = segmentos[i - 1].ycor()
        segmentos[i].goto(x,y)
    
    # Mover el primer segmento
    if len(segmentos) > 0:
        x = ultima_posicion[0]
        y = ultima_posicion[1]
        segmentos[0].goto(x,y)
    
    for segmento in segmentos:
        if segmento.distance(serpiente) < 10:
            reiniciar_juego()
            break
    
    time.sleep(velocidad)