import numpy as np


def matriz_traslacion(tx: float, ty: float, tz: float) -> np.ndarray:
    m = np.eye(4, dtype=float)
    m[0, 3] = tx
    m[1, 3] = ty
    m[2, 3] = tz
    return m


def matriz_escalado(sx: float, sy: float, sz: float) -> np.ndarray:
    m = np.eye(4, dtype=float)
    m[0, 0] = sx
    m[1, 1] = sy
    m[2, 2] = sz
    return m


def matriz_rotacion_x(theta: float) -> np.ndarray:
    c, s = np.cos(theta), np.sin(theta)
    m = np.eye(4, dtype=float)
    m[1, 1] = c
    m[1, 2] = -s
    m[2, 1] = s
    m[2, 2] = c
    return m


def matriz_rotacion_y(theta: float) -> np.ndarray:
    c, s = np.cos(theta), np.sin(theta)
    m = np.eye(4, dtype=float)
    m[0, 0] = c
    m[0, 2] = s
    m[2, 0] = -s
    m[2, 2] = c
    return m


def matriz_rotacion_z(theta: float) -> np.ndarray:
    c, s = np.cos(theta), np.sin(theta)
    m = np.eye(4, dtype=float)
    m[0, 0] = c
    m[0, 1] = -s
    m[1, 0] = s
    m[1, 1] = c
    return m
