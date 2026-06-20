import numpy as np
import sys
import pygame

from model.geometry import crear_cubo, crear_cilindro, crear_piramide, crear_prisma, crear_tetraedro
from model.transform import matriz_traslacion, matriz_escalado, matriz_rotacion_x, matriz_rotacion_y, matriz_rotacion_z
from projection.projections import proyeccion_perspectiva, proyeccion_ortografica, aplicar_proyeccion
from view.camera import Camara
from view.renderer import Renderer3D

def main() -> None:
    figuras = {
        "1": {"nombre": "Cubo", "malla": crear_cubo(1.5)},
        "2": {"nombre": "Pirámide", "malla": crear_piramide(1.5, 2.0)},
        "3": {"nombre": "Cilindro", "malla": crear_cilindro(0.8, 2.0, divisiones=24)},
        "4": {"nombre": "Prisma", "malla": crear_prisma(1.2, 1.2, 1.8)},
        "5": {"nombre": "Tetraedro", "malla": crear_tetraedro(1.5)}
    }
    
    seleccion = "1"
    malla_actual = figuras[seleccion]["malla"]
    
    camara = Camara(posicion=np.array([0.0, 0.0, -8.0]), objetivo=np.array([0.0, 0.0, 0.0]))
    
    matriz_persp = proyeccion_perspectiva(np.pi / 3.0, 1.0, 0.1, 100.0)
    matriz_orto = proyeccion_ortografica()
    
    modo_perspectiva = True
    matriz_proy = matriz_persp

    renderer = Renderer3D(width=800, height=600)
    
    ang_x, ang_y, ang_z = 0.0, 0.0, 0.0
    px, py, pz = 0.0, 0.0, 0.0
    escala = 1.0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                
                if event.key == pygame.K_p:
                    modo_perspectiva = not modo_perspectiva
                    matriz_proy = matriz_persp if modo_perspectiva else matriz_orto

                tecla = pygame.key.name(event.key)
                if tecla in figuras:
                    seleccion = tecla
                    malla_actual = figuras[seleccion]["malla"]

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]: ang_x += 0.03
        if keys[pygame.K_s]: ang_x -= 0.03
        if keys[pygame.K_a]: ang_y += 0.03
        if keys[pygame.K_d]: ang_y -= 0.03
        if keys[pygame.K_q]: ang_z += 0.03
        if keys[pygame.K_e]: ang_z -= 0.03
        
        if keys[pygame.K_LEFT]:  px -= 0.05
        if keys[pygame.K_RIGHT]: px += 0.05
        if keys[pygame.K_UP]:    py += 0.05
        if keys[pygame.K_DOWN]:  py -= 0.05
        
        if keys[pygame.K_r]: escala += 0.02
        if keys[pygame.K_f]: escala = max(0.1, escala - 0.02)

        M = (matriz_traslacion(px, py, pz) @ 
             matriz_rotacion_z(ang_z) @
             matriz_rotacion_y(ang_y) @ 
             matriz_rotacion_x(ang_x) @ 
             matriz_escalado(escala, escala, escala))
        
        puntos = np.stack([v.a_array() for v in malla_actual.vertices])
        puntos_mundo = (M @ puntos.T).T
        puntos_camara = (camara.matriz_vista() @ puntos_mundo.T).T
        puntos_proyectados = aplicar_proyeccion(puntos_camara, matriz_proy)
        puntos_2d = puntos_proyectados[:, :2]

        renderer.clear_screen()
        renderer.dibujar_malla_interactiva(puntos_2d, malla_actual.aristas)
        
        tipo_proy = "Perspectiva" if modo_perspectiva else "Ortográfica"
        renderer.dibujar_interfaz(f"{figuras[seleccion]['nombre']} ({tipo_proy})")
        
        renderer.update_display(60)

    renderer.quit()
    sys.exit()

if __name__ == "__main__":
    main()


"""
EXPLICACIÓN DEL ARCHIVO (Puedes borrar esto antes de entregar):
- Variables de estado: 'ang_x', 'px', 'escala' controlan las transformaciones. Se leen los inputs 
  del teclado para ir incrementando/decrementando estos valores.
- Alternar proyección: Al pulsar la 'P', la variable booleana 'modo_perspectiva' se invierte, y 
  se asigna la matriz correspondiente (ortogonal o perspectiva) a 'matriz_proy'.
- Pipeline MVP: Se combinan las transformaciones multiplicando matrices (usando @ de numpy) en la matriz 'M'. 
  El orden es crucial: M = Traslación * Rotación * Escala. 
- Multiplicación de los puntos: Se extraen los vértices de la malla actual usando 'a_array()' 
  (que les añade el 1 al final para coordenadas homogéneas). Luego se multiplican con la matriz de 
  modelo (M), luego con la de vista de la cámara (V), y finalmente se llama a 'aplicar_proyeccion' 
  para la matriz de proyección (P) con su respectiva división por W.
"""