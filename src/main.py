import numpy as np
from model.geometry import (
    crear_cubo,
    crear_cilindro,
    crear_piramide,
    crear_prisma,
    crear_tetraedro,
)
from model.transform import (
    matriz_traslacion,
    matriz_escalado,
    matriz_rotacion_x,
    matriz_rotacion_y,
    matriz_rotacion_z,
)
from projection.projections import proyeccion_perspectiva, aplicar_proyeccion
from view.camera import Camara
from view.renderer import dibujar_estructura_alambrado, dibujar_estructura_3d


def interpretar_objeto(malla, matriz_transformacion, titulo: str) -> None:
    puntos = np.stack([v.a_array() for v in malla.vertices])
    puntos_mundo = (matriz_transformacion @ puntos.T).T
    puntos_camara = (camara.matriz_vista() @ puntos_mundo.T).T
    puntos_proyectados = aplicar_proyeccion(puntos_camara, matriz_proyeccion)
    puntos_2d = puntos_proyectados[:, :2]
    dibujar_estructura_alambrado(puntos_2d, [(a.inicio, a.fin) for a in malla.aristas], titulo=f"Proyección 2D - {titulo}")
    dibujar_estructura_3d(puntos_mundo[:, :3], [(a.inicio, a.fin) for a in malla.aristas], titulo=f"Vista 3D - {titulo}")


def main() -> None:
    global camara, matriz_proyeccion
    cubo = crear_cubo(1.5)
    cilindro = crear_cilindro(0.8, 2.0, divisiones=24)
    piramide = crear_piramide(1.5, 2.0)
    prisma = crear_prisma(1.2, 1.2, 1.8)
    tetraedro = crear_tetraedro(1.5)

    camara = Camara(
        posicion=np.array([0.0, 0.0, -8.0]),
        objetivo=np.array([0.0, 0.0, 0.0]),
    )
    matriz_proyeccion = proyeccion_perspectiva(np.pi / 3.0, 1.0, 0.1, 100.0)

    interpretar_objeto(
        cubo,
        matriz_traslacion(-3.5, -1.0, 7.0) @ matriz_rotacion_y(np.pi / 6) @ matriz_rotacion_x(np.pi / 12),
        "Cubo",
    )
    interpretar_objeto(
        cilindro,
        matriz_traslacion(3.5, -1.0, 7.0) @ matriz_rotacion_x(np.pi / 24),
        "Cilindro",
    )
    interpretar_objeto(
        piramide,
        matriz_traslacion(-3.5, 2.0, 7.0) @ matriz_rotacion_y(-np.pi / 6) @ matriz_rotacion_x(np.pi / 12),
        "Pirámide",
    )
    interpretar_objeto(
        prisma,
        matriz_traslacion(3.5, 2.0, 7.0) @ matriz_rotacion_z(np.pi / 8) @ matriz_rotacion_x(-np.pi / 12),
        "Prisma",
    )
    interpretar_objeto(
        tetraedro,
        matriz_traslacion(0.0, 3.0, 7.0) @ matriz_rotacion_y(np.pi / 4) @ matriz_rotacion_x(np.pi / 10),
        "Tetraedro",
    )


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
