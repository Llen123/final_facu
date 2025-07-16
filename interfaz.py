import pygame
from datos_globales import *
from utilities import mostrar_texto
from boton import crear_boton, checkear_accion_botones, dibujar_botones

pygame.font.init()
fuente = pygame.font.Font(None, 36)

def dibujar_carta(x, y, carta, imagenes_pokemon, pantalla):
    pygame.draw.rect(pantalla, BLANCO, (x, y, 300, 400), border_radius=10)
    pygame.draw.rect(pantalla, NEGRO, (x, y, 300, 400), 3, border_radius=10)

    nombre_pokemon = carta.get('nombre', 'Desconocido')
    texto_nombre = fuente.render(nombre_pokemon, True, NEGRO)
    pantalla.blit(texto_nombre, (x + 10, y + 10))

    pokemon_nombre = carta.get('nombre')
    if pokemon_nombre and pokemon_nombre.lower() in imagenes_pokemon:
        imagen = imagenes_pokemon[pokemon_nombre.lower()]
        imagen = pygame.transform.scale(imagen, (200, 200))
        pantalla.blit(imagen, (x + 50, y + 50))
    else:
        print(f"No se encontró la imagen de {pokemon_nombre}")

    offset_y = 260
    for atributo, valor in carta.items():
        if atributo != 'nombre':
            texto = fuente.render(f"{atributo.capitalize()}: {valor}", True, NEGRO)
            pantalla.blit(texto, (x + 10, y + offset_y))
            offset_y += 25

def dibujar_cuadro_texto(x, y, ancho, alto, texto, activo, pantalla):
    color = BLANCO if activo else GRIS
    pygame.draw.rect(pantalla, color, (x, y, ancho, alto), 2)
    texto_surface = fuente.render(texto, True, NEGRO)
    pantalla.blit(texto_surface, (x + 10, y + 10))

def mostrar_ventana_ganador(ganador_final, datos_jugadores, pantalla):
    ancho = 600
    alto = 300
    ventana_x = (ANCHO_PANTALLA - ancho) // 2
    ventana_y = (ALTO_PANTALLA - alto) // 2

    fondo_modal = pygame.Surface((ancho, alto))
    fondo_modal.fill(GRIS_OSCURO)
    rect_modal = fondo_modal.get_rect(topleft=(ventana_x, ventana_y))

    fuente_modal = pygame.font.Font(None, 40)

    texto = ""
    if ganador_final[0]:
        texto = f"Ganó {ganador_final[0]} con {datos_jugadores[ganador_final[0]]['puntuacion']} puntos"
    else:
        texto = "¡Empate!"

    botones = [
        crear_boton((150, 50), (ventana_x + 50, ventana_y + 200), pantalla, "Reiniciar"),
        crear_boton((150, 50), (ventana_x + 225, ventana_y + 200), pantalla, "Menú"),
        crear_boton((150, 50), (ventana_x + 400, ventana_y + 200), pantalla, "Salir")
    ]

    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "salir"
            if event.type == pygame.MOUSEBUTTONDOWN:
                accion = checkear_accion_botones(botones, pygame.mouse.get_pos())
                if accion in ["Reiniciar", "Menú", "Salir"]:
                    return accion.lower()

        pantalla.fill(VERDE)
        pantalla.blit(fondo_modal, rect_modal)

        mostrar_texto("Fin del Juego", ventana_x + 200, ventana_y + 30, BLANCO, pantalla, fuente_modal)
        mostrar_texto(texto, ventana_x + 50, ventana_y + 100, BLANCO, pantalla, fuente_modal)

        dibujar_botones(botones, fuente_modal)

        pygame.display.update()

def animar_ventana(ventana_x, ventana_y, ventana_ancho, ventana_alto, pantalla):
    y_inicial = -ventana_alto
    y_final = ventana_y
    velocidad = 10
    for y in range(y_inicial, y_final, velocidad):
        pantalla.fill(VERDE)
        pygame.draw.rect(pantalla, COLOR_VENTANA, (ventana_x, y, ventana_ancho, ventana_alto))
        pygame.draw.rect(pantalla, NEGRO, (ventana_x, y, ventana_ancho, ventana_alto), 3)
        pygame.display.update()
        pygame.time.delay(30)
