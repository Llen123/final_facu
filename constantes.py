# constantes.py

# Colores
VERDE = (0, 255, 0)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
COLOR_BOTON = (100, 100, 255)  # ejemplo

# Fuente
import pygame
pygame.font.init()
FUENTE_PRINCIPAL = pygame.font.Font(None, 36)

# Tamaño de pantalla
ANCHO_PANTALLA = 1280
ALTO_PANTALLA = 720

# Posiciones y dimensiones
POS_CUADRO = (100, 400)
DIM_CUADRO = (300, 50)
POS_VENTANA = (300, 200)

# Criterios
CRITERIOS_ORDENAMIENTO = ["nombre", "puntuacion", "Victorias Elementales"]

# Pokémon incluidos
nombres_pokemon = [
    "aerodactyl", "arcanine", "blastoise", "charizard", "charmander",
    "dragonite", "dugtrio", "electabuzz", "fearow", "flareon",
    "geodude", "golem", "gyarados", "jolteon", "lapras",
    "moltres", "onix", "pidgeot", "pidgeotto", "pikachu",
    "raichu", "sandslash", "squirtle", "vaporeon", "zapdos"
]

# Eventos personalizados
AVANZAR_RONDA = pygame.USEREVENT + 1

# Rutas
RUTA_IMAGENES = "imagenes"
RUTA_FONDO_ESTADIO = "imagenes/fondo_estadio.png"
RUTA_TABLA = "imagenes/fondo_tabla.png"
ARCHIVO_HISTORIAL = "historial_partidas.json"
