#juego de la serpiente

#librerias importadas
import turtle
import time
import random

segmentos = [] # Segmentos de la serpiente guardados

# Valor inicial del Puntaje, Puntaje Maximo, Nivel y Velocidad.
puntaje = 0
puntaje_maximo = 0
nivel = 1
velocidad = 0.1

obstaculos = []

segmentos = [] # Segmentos de la serpiente guardados

# Valor inicial del Puntaje, Puntaje Maximo, Nivel y Velocidad.
puntaje = 0
puntaje_maximo = 0
nivel = 1
velocidad = 0.1

obstaculos = []

pantalla = turtle.Screen()
pantalla.title("Snake")
pantalla.bgcolor("orange")
pantalla.setup(width=600,height=600)
pantalla.tracer(0) # Desactiva la actualizacion de 

# Solicitar el nombre del jugador
nombre_jugador = pantalla.textinput("Nombre del Jugador", "Ingresa tu nombre:")
if not nombre_jugador:
    nombre_jugador = "Anonimo"

#.strip() = borra los espacios del inicio y del final del prompt ingresado
#.lower() = pasa todas las mayusculas a minusculas del prompt ingresado
#/n = salto de linea
#''.join() = signo que separa las lista

# Elegir el color de la serpiente
colores_disponibles = ["darkgreen", "blue", "red", "purple", "orange", "yellow"]
color_serpiente = None

while color_serpiente not in colores_disponibles:
    seleccion_color = pantalla.textinput("Selección de color", f"Elige el color de tu serpiente:\n{' - '.join(colores_disponibles)}")
    if seleccion_color:
        seleccion_color = seleccion_color.lower()
        if seleccion_color in colores_disponibles:
            color_serpiente = seleccion_color
        else: pantalla.textinput ("selección de color", f"Color invalido, Por favor, elige uno de los siguientes:\n{' - '.join(colores_disponibles)}")
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

# Registrar shape personalizado para la cabeza de la serpiente
# Color Verde
turtle.addshape("Diseños/Darkgreen/Snake-Body-Horizontal.gif")
turtle.addshape("Diseños/Darkgreen/Snake-Body-Vertical.gif")
turtle.addshape("Diseños/Darkgreen/Snake-Head-Down.gif")
turtle.addshape("Diseños/Darkgreen/Snake-Head-Left.gif")
turtle.addshape("Diseños/Darkgreen/Snake-Head-Right.gif")
turtle.addshape("Diseños/Darkgreen/Snake-Head-Up.gif")
# Color Azul
turtle.addshape("Diseños/Azul/Snake-Body-Horizontal-Azul.gif")
turtle.addshape("Diseños/Azul/Snake-Body-Vertical-Azul.gif")
turtle.addshape("Diseños/Azul/Snake-Head-Down-Azul.gif")
turtle.addshape("Diseños/Azul/Snake-Head-Left-Azul.gif")
turtle.addshape("Diseños/Azul/Snake-Head-Right-Azul.gif")
turtle.addshape("Diseños/Azul/Snake-Head-Up-Azul.gif")
# Color Rojo
turtle.addshape("Diseños/Rojo/Snake-Body-Horizontal-Rojo.gif")
turtle.addshape("Diseños/Rojo/Snake-Body-Vertical-Rojo.gif")
turtle.addshape("Diseños/Rojo/Snake-Head-Down-Rojo.gif")
turtle.addshape("Diseños/Rojo/Snake-Head-Left-Rojo.gif")
turtle.addshape("Diseños/Rojo/Snake-Head-Right-Rojo.gif")
turtle.addshape("Diseños/Rojo/Snake-Head-Up-Rojo.gif")
#Color Purpura
turtle.addshape("Diseños/Purpura/Snake-Body-Horizontal-Purpura.gif")
turtle.addshape("Diseños/Purpura/Snake-Body-Vertical-Purpura.gif")
turtle.addshape("Diseños/Purpura/Snake-Head-Down-Purpura.gif")
turtle.addshape("Diseños/Purpura/Snake-Head-Left-Purpura.gif")
turtle.addshape("Diseños/Purpura/Snake-Head-Right-Purpura.gif")
turtle.addshape("Diseños/Purpura/Snake-Head-Up-Purpura.gif")
# Color Naranja
turtle.addshape("Diseños/Naranja/Snake-Body-Horizontal-Naranja.gif")
turtle.addshape("Diseños/Naranja/Snake-Body-Vertical-Naranja.gif")
turtle.addshape("Diseños/Naranja/Snake-Head-Down-Naranja.gif")
turtle.addshape("Diseños/Naranja/Snake-Head-Left-Naranja.gif")
turtle.addshape("Diseños/Naranja/Snake-Head-Right-Naranja.gif")
turtle.addshape("Diseños/Naranja/Snake-Head-Up-Naranja.gif")
# Color Amarillo
turtle.addshape("Diseños/Amarillo/Snake-Body-Horizontal-Amarillo.gif")
turtle.addshape("Diseños/Amarillo/Snake-Body-Vertical-Amarillo.gif")
turtle.addshape("Diseños/Amarillo/Snake-Head-Down-Amarillo.gif")
turtle.addshape("Diseños/Amarillo/Snake-Head-Left-Amarillo.gif")
turtle.addshape("Diseños/Amarillo/Snake-Head-Right-Amarillo.gif")
turtle.addshape("Diseños/Amarillo/Snake-Head-Up-Amarillo.gif")
# Usar archivo .gif

color_head_up = "Diseños/Darkgreen/Snake-Head-Up.gif"

match color_serpiente:
    case "darkgreen":
        color_head_horizontal = "Diseños/Darkgreen/Snake-Body-Horizontal.gif"
        color_head_vertical = "Diseños/Darkgreen/Snake-Body-Vertical.gif"
        color_head_down = "Diseños/Darkgreen/Snake-Head-Down.gif"
        color_head_left = "Diseños/Darkgreen/Snake-Head-Left.gif"
        color_head_right = "Diseños/Darkgreen/Snake-Head-Right.gif"
        color_head_up = "Diseños/Darkgreen/Snake-Head-Up.gif"
    case "blue": 
        color_head_horizontal = "Diseños/Azul/Snake-Body-Horizontal-Azul.gif"
        color_head_vertical = "Diseños/Azul/Snake-Body-Vertical-Azul.gif"
        color_head_down = "Diseños/Azul/Snake-Head-Down-Azul.gif"
        color_head_left = "Diseños/Azul/Snake-Head-Left-Azul.gif"
        color_head_right = "Diseños/Azul/Snake-Head-Right-Azul.gif"
        color_head_up = "Diseños/Azul/Snake-Head-Up-Azul.gif"
    case "red":
        color_head_horizontal = "Diseños/Rojo/Snake-Body-Horizontal-Rojo.gif"
        color_head_vertical = "Diseños/Rojo/Snake-Body-Vertical-Rojo.gif"
        color_head_down = "Diseños/Rojo/Snake-Head-Down-Rojo.gif"
        color_head_left = "Diseños/Rojo/Snake-Head-Left-Rojo.gif"
        color_head_right = "Diseños/Rojo/Snake-Head-Right-Rojo.gif"
        color_head_up = "Diseños/Rojo/Snake-Head-Up-Rojo.gif"
    case "purple":
        color_head_horizontal = "Diseños/Purpura/Snake-Body-Horizontal-Purpura.gif"
        color_head_vertical = "Diseños/Purpura/Snake-Body-Vertical-Purpura.gif"
        color_head_down = "Diseños/Purpura/Snake-Head-Down-Purpura.gif"
        color_head_left = "Diseños/Purpura/Snake-Head-Left-Purpura.gif"
        color_head_right = "Diseños/Purpura/Snake-Head-Right-Purpura.gif"
        color_head_up = "Diseños/Purpura/Snake-Head-Up-Purpura.gif"
    case "orange":
        color_head_horizontal = "Diseños/Naranja/Snake-Body-Horizontal-Naranja.gif"
        color_head_vertical = "Diseños/Naranja/Snake-Body-Vertical-Naranja.gif"
        color_head_down = "Diseños/Naranja/Snake-Head-Down-Naranja.gif"
        color_head_left = "Diseños/Naranja/Snake-Head-Left-Naranja.gif"
        color_head_right = "Diseños/Naranja/Snake-Head-Right-Naranja.gif"
        color_head_up = "Diseños/Naranja/Snake-Head-Up-Naranja.gif"
    case "yellow":
        color_head_horizontal = "Diseños/Amarillo/Snake-Body-Horizontal-Amarillo.gif"
        color_head_vertical = "Diseños/Amarillo/Snake-Body-Vertical-Amarillo.gif"
        color_head_down = "Diseños/Amarillo/Snake-Head-Down-Amarillo.gif"
        color_head_left = "Diseños/Amarillo/Snake-Head-Left-Amarillo.gif"
        color_head_right = "Diseños/Amarillo/Snake-Head-Right-Amarillo.gif"
        color_head_up = "Diseños/Amarillo/Snake-Head-Up-Amarillo.gif"

# Cabeza de la serpiente
serpiente = turtle.Turtle()
serpiente.speed(0)
serpiente.shape(color_head_up)  # Shape personalizado
serpiente.penup()
serpiente.goto(0, 0)
serpiente.direction = "stop"

# Función para verificar si un obstáculo está cerca de la serpiente
def esta_cerca_de_serpiente(obstaculo):
    distancia = obstaculo.distance(serpiente)
    return distancia < 50  # Cambia este valor si quieres ajustar la distancia mínima

#comida para la serpiente
comida = turtle.Turtle()
comida.speed(0)
comida.shape("turtle")
comida.color("darkgreen")
comida.penup()
comida.goto(random.randint(-230,230),random.randint(-230,230)) # Envia la comida a una posición random al inicio del juego

# Mostrar el puntaje y nombre del jugador
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write(f"Jugador: {nombre_jugador} Puntaje: {puntaje}  Puntaje mas alto: {puntaje_maximo}    Nivel: {nivel}", align= "center", font =("Arial", 12, "bold"))

# Borrar el texto del puntaje y actualizarlo por el nuevo puntaje
def actualizar_puntaje():
    texto.clear()
    texto.write(f"Jugador: {nombre_jugador} Puntaje: {puntaje}  Puntaje mas alto: {puntaje_maximo}    Nivel: {nivel}", align= "center", font =("Arial", 12, "normal"))

# Actualizar el shape según la dirección
def actualizar_shapes_segmentos():
    for segmento in segmentos:
        # Si esta en direccion Arriba o Abajo usara el shape Vertical
        if serpiente.direction in ["up", "down"]:
            segmento.shape(color_head_vertical)
        # Si esta en la direccion Derecha o Izquierda usara el shape Horizontal
        elif serpiente.direction in ["left", "right"]:
            segmento.shape(color_head_horizontal)

# Obstaculos
def crear_obstaculos():
    for i in range(3):
        obstaculo = turtle.Turtle()
        obstaculo.speed(0)
        obstaculo.shape("circle")
        obstaculo.color("red")
        obstaculo.penup()
        obstaculo.pensize(10)

        # Asignar una dirección aleatoria (horizontal o vertical)
        obstaculo.direction = random.choice(["up", "down", "left", "right"])

        # Generar una posición aleatoria para el obstáculo, asegurándose de que no esté cerca de la serpiente
        while True:
            x = random.randint(-230, 230)
            y = random.randint(-230, 230)
            obstaculo.goto(x, y)

            if not esta_cerca_de_serpiente(obstaculo):
                break  # Si la posición está lo suficientemente lejos, salimos del bucle
        
        obstaculos.append(obstaculo)

crear_obstaculos()

# Función para mover los obstáculos
def mover_obstaculos():
    for obstaculo in obstaculos:
        # Mover en la dirección asignada
        if obstaculo.direction == "up":
            y = obstaculo.ycor()
            obstaculo.sety(y + 10)
        elif obstaculo.direction == "down":
            y = obstaculo.ycor()
            obstaculo.sety(y - 10)
        elif obstaculo.direction == "right":
            x = obstaculo.xcor()
            obstaculo.setx(x + 10)
        elif obstaculo.direction == "left":
            x = obstaculo.xcor()
            obstaculo.setx(x - 10)

        # Rebote de los obstáculos al tocar los bordes
        if obstaculo.xcor() > 240:
            obstaculo.setx(-240)
            obstaculo.direction = "left"  # Cambiar la dirección a la opuesta
        elif obstaculo.xcor() < -240:
            obstaculo.setx(240)
            obstaculo.direction = "right"  # Cambiar la dirección a la opuesta

        if obstaculo.ycor() > 240:
            obstaculo.sety(-240)
            obstaculo.direction = "down"  # Cambiar la dirección a la opuesta
        elif obstaculo.ycor() < -240:
            obstaculo.sety(240)
            obstaculo.direction = "up"  # Cambiar la dirección a la opuesta

        # Verificar si el obstáculo toca la serpiente
        if obstaculo.distance(serpiente) < 30:
            game_over()

        # Verificar si el obstáculo toca algún segmento de la serpiente
        for segmento in segmentos:
            if obstaculo.distance(segmento) < 20:
                game_over()

def rotation_up():
    serpiente.shape(color_head_up)

def rotation_down():
    serpiente.shape(color_head_down)

def rotation_right():
    serpiente.shape(color_head_right)
    
def rotation_left():
    serpiente.shape(color_head_left)

#definir el movimiento de la serpiente
def mover():
    # Mover 20 px hacia Arriba
    if serpiente.direction == "up":
        y = serpiente.ycor()
        serpiente.sety(y + 20)
        rotation_up()
    # Mover 20 px hacia Abajo
    if serpiente.direction == "down":
        y = serpiente.ycor()
        serpiente.sety(y - 20)
        rotation_down()
    # Mover 20 px hacia la Izquierda
    if serpiente.direction == "left":
        x = serpiente.xcor()
        serpiente.setx(x - 20)
        rotation_left()
    # Mover 20 px hacia Derecha
    if serpiente.direction == "right":
        x = serpiente.xcor()
        serpiente.setx(x + 20)
        rotation_right()
    
    actualizar_shapes_segmentos() # Al moverse se actualizara el shape de los segmentos

    # Envoltura de los bordes
    if serpiente.xcor() > 240:
        serpiente.setx(-240)
    elif serpiente.xcor() < -240:
        serpiente.setx(240)
    if serpiente.ycor() > 240:
        serpiente.sety(-240)
    elif serpiente.ycor() < -240:
        serpiente.sety(240) 

# Función para subir de nivel
def subir_nivel():
    global nivel, velocidad_serpiente
    if puntos >= nivel * 50:  # Subir de nivel cada 50 puntos
        nivel += 1
        velocidad_serpiente -= 0.01  # Aumentar la velocidad de la serpiente
        actualizar_puntaje()

# Texto de "Game Over"
texto_game_over = turtle.Turtle()
texto_game_over.speed(0)
texto_game_over.color("white")
texto_game_over.penup()
texto_game_over.hideturtle()

# Mostrar el mensaje de "Game Over"
def game_over():
    # Esconder objetos del juego (serpiente y comida)
    serpiente.hideturtle()
    for segmento in segmentos:
        segmento.hideturtle()
    comida.hideturtle()
    obstaculos.hideturtle()

    texto_game_over.goto(0, 0)
    texto_game_over.write("GAME OVER\nPresiona 'r' para reiniciar", align="center", font=("Arial", 24, "bold"))

# Reiniciar el juego
def reiniciar_juego():
    global puntaje, puntaje_maximo, nivel, velocidad
    serpiente.showturtle()
    comida.showturtle()
    obstaculos.showturtle()
    serpiente.direction = "stop"
    serpiente.goto(0, 0)
    serpiente.goto(0, 0)

    # Ocultar los segmentos
    for segmento in segmentos:
        segmento.goto(1000,1000)
    
    segmentos.clear()  # Limpiar la lista de segmentos agregados
    obstaculos.clear() # Limpiar los obstaculos
    texto_game_over.clear() # Borrar texto
    obstaculos.clear() # Limpiar los obstaculos
    texto_game_over.clear() # Borrar texto

    # Enviar la comida a una ubicación diferente
    comida.goto(random.randint(-230, 230), random.randint(-230, 230))

    # Enviar el obstaculo a otra ubicacion diferente
    obstaculo.goto(random.randint(-230,230),random.randint(-230,230))

    # Reiniciar puntaje, nivel y velocidad
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
pantalla.onkeypress(reiniciar_juego, "r")

# Bucle principal
while True:
    pantalla.update()

    ultima_posicion = serpiente.position()

    mover()

    mover_obstaculo()

    if serpiente.distance(comida) < 20:
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape(color_head_horizontal)
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
        if segmento.distance(serpiente) < 20:
            game_over()
            break

    time.sleep(velocidad)