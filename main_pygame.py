import pygame
import os
from juego import *
from ordenamiento import *
from datos_globales import *
from utilities import mostrar_texto
from boton import * 
from botones_iniciales import *
from interfaz import *
from constantes import *
pygame.init()

pantalla = pygame.display.set_mode((1280, 720))

cuadro_x, cuadro_y2 = POS_CUADRO
cuadro_ancho, cuadro_alto = DIM_CUADRO
ventana_x, ventana_y = POS_VENTANA

botones = crear_botones_juego(pantalla, cuadro_x, cuadro_y2, cuadro_ancho, cuadro_alto, ventana_x, ventana_y)

pygame.display.set_caption("Juego de Cartas Pokémon")
fuente = pygame.font.Font(None, 36)

def cargar_imagenes_pokemon():
    imagenes = {
        nombre: pygame.image.load(os.path.join('imagenes', f"{nombre}.png"))
        for nombre in nombres_pokemon
        if os.path.exists(os.path.join('imagenes', f"{nombre}.png"))
    }

    fondo = os.path.join('imagenes', 'fondo_estadio.png')
    fondo_estadio = pygame.image.load(fondo) if os.path.exists(fondo) else None
    if not fondo_estadio:
        print(f"Advertencia: No se encontró la imagen {fondo}")

    return imagenes, fondo_estadio


def pedir_nombres():
    nombres = {"jugador1": "", "jugador2": ""}
    jugador_actual = "jugador1"
    input_activo = True
    max_caracteres = 15  

    cuadro_ancho = 400
    cuadro_alto = 50
    cuadro_x = (ANCHO_PANTALLA - cuadro_ancho) // 2  
    cuadro_y1 = (ALTO_PANTALLA // 2) - 100  
    cuadro_y2 = (ALTO_PANTALLA // 2) + 20  

    boton_continuar = crear_boton((cuadro_ancho, cuadro_alto), (cuadro_x, cuadro_y2 + 100), pantalla, "continuar")
    boton_menu = crear_boton((cuadro_ancho, cuadro_alto), (cuadro_x, cuadro_y2 + 160), pantalla, "menu")
  

    while input_activo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    jugador_actual = "jugador2" if jugador_actual == "jugador1" else jugador_actual
                    input_activo = jugador_actual == "jugador1"
                elif event.key == pygame.K_BACKSPACE:
                    nombres[jugador_actual] = nombres[jugador_actual][:-1]
                elif len(nombres[jugador_actual]) < max_caracteres:
                    nombres[jugador_actual] += event.unicode


            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                if (cuadro_x <= mouse_pos[0] <= cuadro_x + cuadro_ancho and
                    cuadro_y1 <= mouse_pos[1] <= cuadro_y1 + cuadro_alto):
                    jugador_actual = "jugador1"
                
                elif (cuadro_x <= mouse_pos[0] <= cuadro_x + cuadro_ancho and
                      cuadro_y2 <= mouse_pos[1] <= cuadro_y2 + cuadro_alto):
                    jugador_actual = "jugador2"
                
                accion = checkear_accion_botones([boton_continuar, boton_menu], mouse_pos)
                if accion == "Continuar":
                    if nombres["jugador1"] and nombres["jugador2"]:
                        input_activo = False
                elif accion == "Volver al Menú":
                    return "menu"

        pantalla.fill(VERDE)
        dibujar_cuadro_texto(cuadro_x, cuadro_y1, cuadro_ancho, cuadro_alto, nombres["jugador1"], jugador_actual == "jugador1", pantalla)
        dibujar_cuadro_texto(cuadro_x, cuadro_y2, cuadro_ancho, cuadro_alto, nombres["jugador2"], jugador_actual == "jugador2", pantalla)

        dibujar_botones([boton_continuar, boton_menu], fuente)

        texto_instrucciones = fuente.render("Ingresa los nombres de los jugadores", True, NEGRO)
        texto_instrucciones_rect = texto_instrucciones.get_rect(center=(ANCHO_PANTALLA // 2, cuadro_y1 - 50))
        pantalla.blit(texto_instrucciones, texto_instrucciones_rect)

        texto_limite = fuente.render(f"Máximo {max_caracteres} caracteres", True, NEGRO)
        texto_limite_rect = texto_limite.get_rect(center=(ANCHO_PANTALLA // 2, cuadro_y1 - 20))
        pantalla.blit(texto_limite, texto_limite_rect)

        pygame.display.update()

    return nombres

def mostrar_tabla_posiciones(criterio, orden):
    tabla_pantalla = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Tabla de Posiciones")

    fondo_tabla = RUTA_TABLA
    fondo_tabla = pygame.transform.scale(fondo_tabla, (1280, 720))

    fuente = pygame.font.Font(None, 36)

    archivo_json = "historial_partidas.json"
    historial_partidas = manejar_archivo_json(archivo_json, "leer")
    jugadores_del_historial = obtener_jugadores_del_historial(historial_partidas)
    jugadores_ordenados = bubble_sort(jugadores_del_historial, criterio, orden)

    boton_menu = crear_boton((280, 50), (500, 600), tabla_pantalla, "Volver al Menú")
    dibujar_botones([boton_menu], fuente)


    running = True
    while running:
        tabla_pantalla.blit(fondo_tabla, (0, 0))
        mostrar_texto("Tabla de Posiciones", 500, 50, BLANCO, tabla_pantalla, fuente)

        y = 150
        contador = 0

        for i, jugador in enumerate(jugadores_ordenados):
            if i >= 6:
                break

            texto_fecha = f"Fecha: {jugador['Fecha Partida']}"
            texto_nombre = f"Nombre: {jugador['nombre']}"
            texto_puntuacion = f"Puntuación: {jugador['puntuacion']}"
            texto_victorias = f"Victorias Elementales: {jugador['Victorias Elementales']}"

            if i < 3:
                x = 200
            else:
                x = 800

            mostrar_texto(texto_fecha, x, y, BLANCO, tabla_pantalla, fuente)
            y += 30
            mostrar_texto(texto_nombre, x, y, BLANCO, tabla_pantalla, fuente)
            y += 30
            mostrar_texto(texto_puntuacion, x, y, BLANCO, tabla_pantalla, fuente)
            y += 30
            mostrar_texto(texto_victorias, x, y, BLANCO, tabla_pantalla, fuente)
            y += 40

            contador += 1
            if contador == 3:
                y = 150

        pygame.draw.rect(tabla_pantalla, COLOR_BOTON, boton_menu)
        texto_volver = fuente.render("Volver al Menú", True, BLANCO)
        texto_volver_rect = texto_volver.get_rect(center=boton_menu.center)
        tabla_pantalla.blit(texto_volver, texto_volver_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                accion = checkear_accion_botones([boton_menu], event.pos)
                if accion == "Volver al Menú":
                    running = False

        pygame.display.update()

    pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

def main():
    imagenes_pokemon, fondo_estadio = cargar_imagenes_pokemon()

    nombres = pedir_nombres()
    if nombres == "menu":
        from menu_pygame import menu_principal
        menu_principal()
        return
    elif not nombres:
        return

    datos_jugadores = {
        "jugador1": {"nombre": nombres["jugador1"], "puntuacion": 0, "Victorias Elementales": 0},
        "jugador2": {"nombre": nombres["jugador2"], "puntuacion": 0, "Victorias Elementales": 0},
    }
    mazo_jugadores = preparar_mazo()
    mesas = []
    max_rondas = 250
    ronda = 1

    estado_juego = "jugando"
    ganador_final = None
    atributo_elegido = None
    resultado_comparacion = None

    AVANZAR_RONDA = pygame.USEREVENT + 1
    pygame.time.set_timer(AVANZAR_RONDA, 1000)

    botones = crear_botones_juego(pantalla, cuadro_x, cuadro_y2, cuadro_ancho, cuadro_alto, ventana_x, ventana_y)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                accion = checkear_accion_botones(botones["velocidad"], mouse_pos)

                if accion == "Rápido":
                    pygame.time.set_timer(AVANZAR_RONDA, 100)
                elif accion == "Normal":
                    pygame.time.set_timer(AVANZAR_RONDA, 500)
                elif accion == "Lento":
                    pygame.time.set_timer(AVANZAR_RONDA, 1000)

            if event.type == AVANZAR_RONDA and estado_juego == "jugando":
                print(f"Iniciando ronda {ronda}")
                resultado_ronda = jugar_ronda(ronda, datos_jugadores, mazo_jugadores, mesas)

                ganador_ronda = resultado_ronda["ganador"]
                nombre_ganador = resultado_ronda["nombre_ganador"]
                atributo_elegido = resultado_ronda["atributo_elegido"]
                resultado_comparacion = resultado_ronda["resultado_comparacion"]

                ganador_final = verificar_condiciones_de_victoria(datos_jugadores, mazo_jugadores, ronda, max_rondas)
                if ganador_final[0]:
                    print(f"¡Ganador final: {ganador_final[0]}!")
                    estado_juego = "fin"
                    guardar_datos_jugadores(datos_jugadores, ganador_final[0])
                elif ganador_final[0] is None and ganador_final[1]:
                    print("¡Empate!")
                    estado_juego = "fin"
                    guardar_datos_jugadores(datos_jugadores, None)
                else:
                    estado_juego = "resultado"
                    ronda += 1

            if event.type == AVANZAR_RONDA and estado_juego == "resultado":
                estado_juego = "jugando"

        if fondo_estadio:
            pantalla.blit(fondo_estadio, (0, 0))
        else:
            pantalla.fill(VERDE)

        if mazo_jugadores["jugador1"] and mazo_jugadores["jugador2"]:
            carta_jugador1 = mazo_jugadores["jugador1"][0]
            carta_jugador2 = mazo_jugadores["jugador2"][0]

            dibujar_carta(200, 160, carta_jugador1, imagenes_pokemon, pantalla)
            dibujar_carta(800, 160, carta_jugador2, imagenes_pokemon, pantalla)


        # Dibujo botones de velocidad
        dibujar_botones(botones["velocidad"], fuente)

        mostrar_texto(f"Ronda: {ronda}", 10, 10, BLANCO, pantalla, fuente)
        if atributo_elegido:
            mostrar_texto(f"Atributo elegido: {atributo_elegido}", 10, 50, BLANCO, pantalla, fuente)
        if resultado_comparacion:
            if resultado_ronda["ganador"]:
                mostrar_texto(f"Ganador de la ronda actual: {resultado_ronda['nombre_ganador']}", 10, 90, BLANCO, pantalla, fuente)
            else:
                mostrar_texto(resultado_ronda["resultado_comparacion"], 10, 90, BLANCO, pantalla, fuente)

        if estado_juego == "fin":
            resultado = mostrar_ventana_ganador(ganador_final, datos_jugadores, pantalla)
            if resultado == "reiniciar":
                main()
            elif resultado == "menu":
                from menu_pygame import menu_principal
                menu_principal()
                running = False
            elif resultado == "salir":
                running = False

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()