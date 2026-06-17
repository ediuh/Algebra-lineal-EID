import numpy as np


class Camara:
    def __init__(self, posicion: np.ndarray, objetivo: np.ndarray, arriba: np.ndarray = None):
        self.posicion = posicion
        self.objetivo = objetivo
        self.arriba = np.array([0.0, 1.0, 0.0]) if arriba is None else arriba

    def matriz_vista(self) -> np.ndarray:
        adelante = self.objetivo - self.posicion
        adelante = adelante / np.linalg.norm(adelante)
        derecha = np.cross(self.arriba, adelante)
        derecha = derecha / np.linalg.norm(derecha)
        arriba_real = np.cross(adelante, derecha)

        m = np.eye(4, dtype=float)
        m[0, :3] = derecha
        m[1, :3] = arriba_real
        m[2, :3] = adelante
        m[0, 3] = -np.dot(derecha, self.posicion)
        m[1, 3] = -np.dot(arriba_real, self.posicion)
        m[2, 3] = -np.dot(adelante, self.posicion)
        return m
