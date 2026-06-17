# Mini Motor 3D - Álgebra Lineal

Estructura de proyecto para un mini motor 3D con Modelo-Vista-Proyección (MVP).

## Estructura de carpetas

- `src/`
  - `model/`
    - `geometry.py` - definición de vértices, aristas y mallas.
    - `transform.py` - matrices de transformación homogénea.
  - `view/`
    - `camera.py` - cámara y matriz de vista.
    - `renderer.py` - renderizado de proyección 2D.
  - `projection/`
    - `projections.py` - proyecciones ortográfica y perspectiva.
  - `main.py` - ejemplo de uso del pipeline MVP.

## Requisitos

- Python 3.14+
- NumPy
- Matplotlib

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
python src/main.py
```
