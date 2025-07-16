from boton import crear_boton

from boton import crear_boton

def crear_botones_juego(pantalla, cuadro_x, cuadro_y2, cuadro_ancho, cuadro_alto, ventana_x, ventana_y):
    botones = {}

    botones["velocidad"] = [
        crear_boton((120, 40), (1000, 10), pantalla, "Rápido"),
        crear_boton((120, 40), (1000, 60), pantalla, "Normal"),
        crear_boton((120, 40), (1000, 110), pantalla, "Lento")
    ]

    botones["cuadro"] = [
        crear_boton((cuadro_ancho, cuadro_alto), (cuadro_x, cuadro_y2 + 100), pantalla, "Continuar"),
        crear_boton((cuadro_ancho, cuadro_alto), (cuadro_x, cuadro_y2 + 160), pantalla, "Menú")
    ]

    botones["fin"] = [
        crear_boton((200, 50), (ventana_x + 50, ventana_y + 200), pantalla, "Reiniciar"),
        crear_boton((200, 50), (ventana_x + 300, ventana_y + 200), pantalla, "Menú")
    ]

    return botones
