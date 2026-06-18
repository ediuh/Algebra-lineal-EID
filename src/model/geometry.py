import numpy as np
from dataclasses import dataclass
from typing import List

Vector3 = np.ndarray

@dataclass
class Vertice:
    x: float
    y: float
    z: float

    def a_array(self) -> Vector3:
        return np.array([self.x, self.y, self.z, 1.0])

@dataclass
class Arista:
    inicio: int
    fin: int

@dataclass
class Malla:
    vertices: List[Vertice]
    aristas: List[Arista]

    def transformar(self, matriz: np.ndarray) -> "Malla":
        transformados = [Vertice(*((matriz @ v.a_array())[:3])) for v in self.vertices]
        return Malla(transformados, self.aristas)


def crear_cubo(tamano: float = 1.0) -> Malla:
    mitad = tamano / 2.0
    vertices = [
        Vertice(-mitad, -mitad, -mitad),
        Vertice(mitad, -mitad, -mitad),
        Vertice(mitad, mitad, -mitad),
        Vertice(-mitad, mitad, -mitad),
        Vertice(-mitad, -mitad, mitad),
        Vertice(mitad, -mitad, mitad),
        Vertice(mitad, mitad, mitad),
        Vertice(-mitad, mitad, mitad),
    ]
    aristas = [
        Arista(0, 1), Arista(1, 2), Arista(2, 3), Arista(3, 0),
        Arista(4, 5), Arista(5, 6), Arista(6, 7), Arista(7, 4),
        Arista(0, 4), Arista(1, 5), Arista(2, 6), Arista(3, 7),
    ]
    return Malla(vertices, aristas)


def crear_piramide(tamano: float = 1.0, altura: float = 1.0) -> Malla:
    mitad = tamano / 2.0
    vertices = [
        Vertice(-mitad, -mitad, 0.0),
        Vertice(mitad, -mitad, 0.0),
        Vertice(mitad, mitad, 0.0),
        Vertice(-mitad, mitad, 0.0),
        Vertice(0.0, 0.0, altura),
    ]
    aristas = [
        Arista(0, 1), Arista(1, 2), Arista(2, 3), Arista(3, 0),
        Arista(0, 4), Arista(1, 4), Arista(2, 4), Arista(3, 4),
    ]
    return Malla(vertices, aristas)


def crear_prisma(ancho: float = 1.0, profundidad: float = 1.0, altura: float = 1.0) -> Malla:
    ha = ancho / 2.0
    hp = profundidad / 2.0
    vertices = [
        Vertice(-ha, -hp, 0.0),
        Vertice(ha, -hp, 0.0),
        Vertice(0.0, hp, 0.0),
        Vertice(-ha, -hp, altura),
        Vertice(ha, -hp, altura),
        Vertice(0.0, hp, altura),
    ]
    aristas = [
        Arista(0, 1), Arista(1, 2), Arista(2, 0),
        Arista(3, 4), Arista(4, 5), Arista(5, 3),
        Arista(0, 3), Arista(1, 4), Arista(2, 5),
    ]
    return Malla(vertices, aristas)


def crear_cilindro(radio: float = 1.0, altura: float = 2.0, divisiones: int = 16) -> Malla:
    vertices = []
    aristas = []
    for i in range(divisiones):
        angulo = 2.0 * np.pi * i / divisiones
        x = radio * np.cos(angulo)
        y = radio * np.sin(angulo)
        vertices.append(Vertice(x, y, 0.0))
    for i in range(divisiones):
        angulo = 2.0 * np.pi * i / divisiones
        x = radio * np.cos(angulo)
        y = radio * np.sin(angulo)
        vertices.append(Vertice(x, y, altura))

    for i in range(divisiones):
        aristas.append(Arista(i, (i + 1) % divisiones))
        aristas.append(Arista(i + divisiones, ((i + 1) % divisiones) + divisiones))
        aristas.append(Arista(i, i + divisiones))

    return Malla(vertices, aristas)


def crear_tetraedro(tamano: float = 1.0) -> Malla:
    altura = tamano * np.sqrt(2.0 / 3.0)
    vertices = [
        Vertice(0.0, 0.0, 0.0),
        Vertice(tamano, 0.0, 0.0),
        Vertice(tamano / 2.0, tamano * np.sqrt(3) / 2.0, 0.0),
        Vertice(tamano / 2.0, tamano * np.sqrt(3) / 6.0, altura),
    ]
    aristas = [
        Arista(0, 1), Arista(1, 2), Arista(2, 0),
        Arista(0, 3), Arista(1, 3), Arista(2, 3),
    ]
    return Malla(vertices, aristas)
