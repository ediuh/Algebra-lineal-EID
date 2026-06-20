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



# ==============================================================================
# EXPLICACIÓN MATEMÁTICA: Mover el Objeto vs. Mover la Cámara
# ==============================================================================
# El objetivo de la renderización es llevar vértices de un "espacio de modelo"
# a un "espacio de pantalla". Esto se logra a través de una cadena de
# transformaciones de coordenadas.
#
# La relación fundamental para obtener el vértice proyectado (V_p) es:
# V_p = P * V * M * V_orig
# Donde:
#   V_orig: Coordenadas del vértice en su propio sistema local (Modelo).
#   M: Matriz de Modelo. Transforma de espacio local a Espacio del Mundo.
#   V: Matriz de Vista (Cámara). Transforma de Espacio del Mundo a Espacio de la Cámara.
#   P: Matriz de Proyección. Transforma de Espacio de la Cámara a Espacio de Pantalla.
#
# La diferencia clave radica en qué matriz se modifica y cómo afecta a los vértices.
#
# 1. MOVER EL OBJETO (Matriz M):
# Al mover el objeto, modificamos su Matriz de Modelo (M). Matemáticamente, estamos
# aplicando una transformación de traslación, rotación o escalado (M = T * R * S)
# a cada vértice local (V_orig). Esto cambia la posición y orientación del objeto
# DENTRO DEL MUNDO, pero la cámara sigue viendo el mundo desde el mismo punto.
# El cálculo se ve así:
# V_mundo_nuevo = (T_nueva * R_nueva * S) * V_orig
# V_camara = V * V_mundo_nuevo
#
# 2. MOVER LA CÁMARA (Matriz V):
# Al mover la cámara, modificamos la Matriz de Vista (V). La cámara no altera el
# mundo en sí (la matriz M permanece igual), sino cómo lo "percibimos".
# Matemáticamente, la matriz de vista transforma el mundo para que la cámara actúe
# como el origen del nuevo sistema de coordenadas. Mover la cámara de forma
# "natural" es matemáticamente equivalente a aplicar la transformación INVERSA a
# todo el mundo.
# Si queremos mover la cámara a la posición (Cx, Cy, Cz), la matriz de vista (V)
# debe incluir una traslación de T(-Cx, -Cy, -Cz). Por eso se dice que para mover
# la cámara hacia adelante, ¡matemáticamente traemos todo el mundo hacia atrás!
# El cálculo se ve así:
# V_mundo_viejo = M * V_orig  (el objeto no se mueve en el mundo)
# V_camara_nueva = (T_camara_inversa * R_camara_inversa) * V_mundo_viejo
#
# EN RESUMEN:
# Mover el objeto altera su posición/rotación absoluta en el espacio 3D (cambia M).
# Mover la cámara altera el sistema de referencia desde el cual se observan los
# objetos, lo que es matemáticamente equivalente a aplicar la transformación opuesta
# a todos los objetos del mundo (cambia V). En ambos casos, el resultado visual
# cambia, pero la causa matemática es distinta.
# ==============================================================================