import pygame
import webbrowser
from ordenamiento import *
from main_pygame import *
from utilities import mostrar_texto
from datos_globales import *

pygame.init()

pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Menú Principal")

icono_ventana = pygame.image.load("imagenes/icono.png")
pygame.display.set_icon(icono_ventana)

fuente = pygame.font.Font(None, 50)
fuente_pequena = pygame.font.Font(None, 30)

fondo_menu = pygame.image.load("imagenes/fondo_menu.png")
fondo_menu = pygame.transform.scale(fondo_menu, (ANCHO_PANTALLA, ALTO_PANTALLA))

from boton import crear_boton, dibujar_botones, checkear_accion_botones

def menu_principal():
    ejecutando = True

    padding = 20
    menu_x = padding
    menu_y = padding
    menu_ancho = 400
    menu_alto = ALTO_PANTALLA - 2 * padding

    botones = [
        crear_boton((menu_ancho - 2 * padding, 60), (menu_x + padding, menu_y + 120), pantalla, "Jugar"),
        crear_boton((menu_ancho - 2 * padding, 60), (menu_x + padding, menu_y + 285), pantalla, "Ver historial"),
        crear_boton((menu_ancho - 2 * padding, 60), (menu_x + padding, menu_y + 450), pantalla, "Salir")
    ]

    while ejecutando:
        pantalla.blit(fondo_menu, (0, 0))
        pygame.draw.rect(pantalla, GRIS_OSCURO, (menu_x, menu_y, menu_ancho, menu_alto))
        mostrar_texto('Menú Principal', menu_x + padding, menu_y + padding, BLANCO, pantalla, fuente)

        dibujar_botones(botones, fuente)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutando = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                accion = checkear_accion_botones(botones, pygame.mouse.get_pos())
                if accion == "Jugar":
                    from main_pygame import main
                    main()
                    ejecutando = False
                elif accion == "Ver historial":
                    mostrar_tabla_posiciones(criterio="puntuacion", orden="desc")
                elif accion == "Salir":
                    ejecutando = False

        pygame.display.flip()

if __name__ == "__main__":
    menu_principal()