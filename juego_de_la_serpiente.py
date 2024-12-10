import turtle
import time
import random

# Constantes
TAMANIO_LIMITE = 500
VELOCIDAD_INICIAL = 0.1
COLORES_DISPONIBLES = ["darkgreen", "blue", "red", "purple", "orange", "yellow"]

# Configuración inicial de pantalla
pantalla = turtle.Screen()
pantalla.title("Snake")
pantalla.bgcolor("green")
pantalla.setup(width=600, height=600)
pantalla.tracer(0)

# Solicitar nombre del jugador
nombre_jugador = pantalla.textinput("Nombre del Jugador", "Ingresa tu nombre:") or "Anónimo"

# Selección de color
def elegir_color():
    while True:
        color = pantalla.textinput(
            "Selección de color",
            f"Elige el color de tu serpiente:\n{' - '.join(COLORES_DISPONIBLES)}"
        )
        if not color:
            return "darkgreen"
        color = color.strip().lower()
        if color in COLORES_DISPONIBLES:
            return color
        pantalla.textinput("Error", "Color inválido. Se asignó 'darkgreen' por defecto.")
        return "darkgreen"

color_serpiente = elegir_color()

# Dibujar borde del juego
linea_limite = turtle.Turtle()
linea_limite.speed(0)
linea_limite.color("white")
linea_limite.penup()
linea_limite.goto(-TAMANIO_LIMITE // 2, -TAMANIO_LIMITE // 2)
linea_limite.pendown()
linea_limite.pensize(10)
for _ in range(4):
    linea_limite.forward(TAMANIO_LIMITE)
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

# Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("darkgreen")
comida.penup()
comida.goto(random.randint(-230, 230), random.randint(-230, 230))

# Texto del puntaje
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 260)

puntaje, puntaje_maximo, nivel, velocidad = 0, 0, 1, VELOCIDAD_INICIAL
segmentos = []

def actualizar_puntaje():
    texto.clear()
    texto.write(f"Jugador: {nombre_jugador} Puntaje: {puntaje}  Puntaje más alto: {puntaje_maximo}  Nivel: {nivel}", align="center", font=("Arial", 12, "bold"))

actualizar_puntaje()

# Movimiento de la serpiente
def mover():
    x, y = serpiente.xcor(), serpiente.ycor()
    if serpiente.direction == "up":
        serpiente.sety(y + 20)
    elif serpiente.direction == "down":
        serpiente.sety(y - 20)
    elif serpiente.direction == "left":
        serpiente.setx(x - 20)
    elif serpiente.direction == "right":
        serpiente.setx(x + 20)

    # Envoltura
    if serpiente.xcor() > TAMANIO_LIMITE // 2 - 10:
        serpiente.setx(-TAMANIO_LIMITE // 2 + 10)
    elif serpiente.xcor() < -TAMANIO_LIMITE // 2 + 10:
        serpiente.setx(TAMANIO_LIMITE // 2 - 10)
    if serpiente.ycor() > TAMANIO_LIMITE // 2 - 10:
        serpiente.sety(-TAMANIO_LIMITE // 2 + 10)
    elif serpiente.ycor() < -TAMANIO_LIMITE // 2 + 10:
        serpiente.sety(TAMANIO_LIMITE // 2 - 10)

# Controles
def arriba(): serpiente.direction = "up" if serpiente.direction != "down" else serpiente.direction
def abajo(): serpiente.direction = "down" if serpiente.direction != "up" else serpiente.direction
def izquierda(): serpiente.direction = "left" if serpiente.direction != "right" else serpiente.direction
def derecha(): serpiente.direction = "right" if serpiente.direction != "left" else serpiente.direction

pantalla.listen()
pantalla.onkeypress(arriba, "Up")
pantalla.onkeypress(abajo, "Down")
pantalla.onkeypress(izquierda, "Left")
pantalla.onkeypress(derecha, "Right")

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

# Bucle principal
while True:
    pantalla.update()

    ultima_posicion = serpiente.position()

    mover()

    if serpiente.distance(comida) < 20:
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("circle")
        nuevo_segmento.color(color_serpiente)
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