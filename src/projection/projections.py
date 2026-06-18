import numpy as np


def proyeccion_ortografica() -> np.ndarray:
    m = np.eye(4, dtype=float)
    m[2, 2] = 0.0
    return m


def proyeccion_perspectiva(fov: float, aspect: float, near: float, far: float) -> np.ndarray:
    f = 1.0 / np.tan(fov / 2.0)
    m = np.zeros((4, 4), dtype=float)
    m[0, 0] = f / aspect
    m[1, 1] = f
    m[2, 2] = (far + near) / (near - far)
    m[2, 3] = (2 * far * near) / (near - far)
    m[3, 2] = -1.0
    return m


def aplicar_proyeccion(puntos: np.ndarray, matriz: np.ndarray) -> np.ndarray:
    transformados = (matriz @ puntos.T).T
    w = transformados[:, 3:4]
    return transformados[:, :3] / np.where(w == 0, 1, w)
