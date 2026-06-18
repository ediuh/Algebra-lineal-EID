import numpy as np


class Camara:
    def __init__(self, posicion: np.ndarray, objetivo: np.ndarray, arriba: np.ndarray = None):
        self.posicion = np.array(posicion, dtype=float)
        self.objetivo = np.array(objetivo, dtype=float)
        self.arriba = (
            np.array([0.0, 1.0, 0.0]) if arriba is None else np.array(arriba, dtype=float)
        )

    def mover_a(self, nueva_posicion: np.ndarray) -> None:
        self.posicion = np.array(nueva_posicion, dtype=float)
    
    def apuntar_a(self, nuevo_objetivo: np.ndarray) -> None:
        self.objetivo = np.array(nuevo_objetivo, dtype=float)

    def matriz_vista(self) -> np.ndarray:
        adelante = self.objetivo - self.posicion
        norma_adelante = np.linalg.norm(adelante)
        if norma_adelante < 1e-10:
            raise ValueError("La posición y el objetivo no pueden ser iguales.")
        adelante = adelante / np.linalg.norm(adelante)


        derecha = np.cross(self.arriba, adelante)
        norma_derecha = np.linalg.norm(derecha)
        if norma_derecha < 1e-10:
            raise ValueError("El vector 'arriba' no puede ser paralelo al vector 'adelante'.")
        derecha = derecha / np.linalg.norm(derecha)

        
        arriba_real = np.cross(adelante, derecha)
        arriba_real = arriba_real / np.linalg.norm(arriba_real)

        m = np.eye(4, dtype=float)
        m[0, :3] = derecha
        m[1, :3] = arriba_real
        m[2, :3] = adelante
        m[0, 3] = -np.dot(derecha, self.posicion)
        m[1, 3] = -np.dot(arriba_real, self.posicion)
        m[2, 3] = -np.dot(adelante, self.posicion)
        return m

camara  = Camara(
    posicion=np.array([0.0, 0.0, -8.0]),
    objetivo=np.array([0.0, 0.0, 0.0]),
)
# Mover la cámara y volver a renderizar
camara.mover_a([2.0, 1.0, -8.0])
camara.apuntar_a([0.0, 0.0, 0.0])
