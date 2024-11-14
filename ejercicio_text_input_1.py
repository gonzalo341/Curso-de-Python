#Cuadro de Texto
import turtle

pantalla = turtle.Screen()
pantalla.title("Dibujar una linea recta")
pantalla.bgcolor("white")

nombre_de_usuario = pantalla.textinput(
    "Nombre del usuario",
    "Ingrese su nombre" 
) 
if nombre_de_usuario == (""):
    jugador = "Anonimo"

color_de_pantalla = pantalla.textinput(
    "color de pantalla",
    "white,black,red,green,blue,yellow,"
)

pantalla.bgcolor(color_de_pantalla)

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

pantalla.mainloop()