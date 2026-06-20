import pygame
import numpy as np
from typing import List

class Renderer3D:
    def __init__(self, width: int = 800, height: int = 600):
        pygame.init()
        pygame.font.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Mini Motor 3D")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 18)
        
    def clear_screen(self):
        self.screen.fill((18, 18, 24))
        
    def dibujar_malla_interactiva(self, puntos_2d: np.ndarray, aristas: List) -> None:
        cx = self.width // 2
        cy = self.height // 2
        escala = 150 
        
        for arista in aristas:
            inicio = arista.inicio
            fin = arista.fin
            
            x1, y1 = puntos_2d[inicio, 0], puntos_2d[inicio, 1]
            x2, y2 = puntos_2d[fin, 0], puntos_2d[fin, 1]
            
            px1 = int(cx + x1 * escala)
            py1 = int(cy - y1 * escala)
            px2 = int(cx + x2 * escala)
            py2 = int(cy - y2 * escala)
            
            pygame.draw.line(self.screen, (0, 255, 190), (px1, py1), (px2, py2), 2)
            
    def dibujar_interfaz(self, nombre_figura: str):
        instrucciones = [
            f"Figura Actual: {nombre_figura}",
            "Cambiar Figura: 1 al 5",
            "Rotar: W/S (X) | A/D (Y) | Q/E (Z)",
            "Trasladar: Flechas",
            "Escalar: R (+) | F (-)"
        ]
        
        for idx, texto in enumerate(instrucciones):
            color = (255, 255, 255) if idx == 0 else (150, 150, 160)
            superficie = self.font.render(texto, True, color)
            self.screen.blit(superficie, (20, 20 + idx * 22))
            
    def update_display(self, fps: int = 60):
        pygame.display.flip()
        self.clock.tick(fps)
        
    def quit(self):
        pygame.quit()


"""
EXPLICACIÓN DEL ARCHIVO (Puedes borrar esto antes de entregar):
- dibujar_malla_interactiva: Toma los puntos 2D procesados por el main. Multiplica por una 'escala' 
  para que el objeto no se vea enano. Se suma 'cx' y se resta 'cy' (py1 = int(cy - y1 * escala)) 
  para trasladar el (0,0) que está en la esquina superior izquierda de Pygame hacia el centro de la pantalla. 
  Se invierte el eje Y porque en computación crece hacia abajo, pero en álgebra crece hacia arriba.
- dibujar_interfaz: Renderiza textos simples iterando sobre una lista y posicionándolos con un offset 
  vertical (idx * 22).
"""