import matplotlib.pyplot as plt
import numpy as np
from typing import List


def proyectar_puntos(puntos: List[np.ndarray]) -> np.ndarray:
    proyeccion = np.stack(puntos)
    return proyeccion[:, :2]


def dibujar_estructura_alambrado(puntos: List[np.ndarray], aristas: List[tuple[int, int]], titulo: str = "Estructura de alambre") -> None:
    proyeccion = proyectar_puntos(puntos)
    fig, ax = plt.subplots()
    for inicio, fin in aristas:
        xs = [proyeccion[inicio, 0], proyeccion[fin, 0]]
        ys = [proyeccion[inicio, 1], proyeccion[fin, 1]]
        ax.plot(xs, ys, color="black")
    ax.set_aspect("equal")
    ax.set_title(titulo)
    plt.show()


def dibujar_estructura_3d(puntos: List[np.ndarray], aristas: List[tuple[int, int]], titulo: str = "Visualización 3D") -> None:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    for inicio, fin in aristas:
        xs = [puntos[inicio][0], puntos[fin][0]]
        ys = [puntos[inicio][1], puntos[fin][1]]
        zs = [puntos[inicio][2], puntos[fin][2]]
        ax.plot(xs, ys, zs, color="black")

    all_points = np.stack(puntos)
    ax.scatter(all_points[:, 0], all_points[:, 1], all_points[:, 2], color="red", s=20)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title(titulo)
    ax.set_box_aspect([1, 1, 1])
    plt.show()
