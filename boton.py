import pygame
def crear_boton(dimensiones, posicion, ventana, accion, imagen=None):
    boton = {}
    boton["Ventana"] = ventana
    boton["Dimensiones"] = dimensiones
    boton["Posicion"] = posicion
    boton["Presionado"] = False
    boton["Accion"] = accion

    if imagen is not None:
        img = pygame.image.load(imagen)
        boton["Contenido"] = pygame.transform.scale(img, boton["Dimensiones"])
    else:
        superficie = pygame.Surface(dimensiones)
        superficie.fill((100, 100, 100)) 
        boton["Contenido"] = superficie

    boton["Rectangulo"] = boton["Contenido"].get_rect()
    boton["Rectangulo"].topleft = boton["Posicion"]

    return boton


def dibujar(boton):
    boton["Ventana"].blit(boton["Contenido"], boton["Posicion"])

def dibujar_botones(lista_botones, fuente):
    for boton in lista_botones:
        boton["Ventana"].blit(boton["Contenido"], boton["Posicion"])
        if fuente:  
            texto = fuente.render(boton["Accion"], True, (255, 255, 255))
            rect = texto.get_rect(center=boton["Rectangulo"].center)
            boton["Ventana"].blit(texto, rect)


def checkear_accion_botones(lista_botones, mouse_pos):
    for boton in lista_botones:
        if boton["Rectangulo"].collidepoint(mouse_pos):
            return boton["Accion"]
    return None





