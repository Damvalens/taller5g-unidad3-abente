# taller5g-unidad3-abente

**Alumno:** Celso Daniel Abente Valenzuela  
**Apellido:** Abente  
**Materia:** Taller de Programación de 5.ª Generación I  
**Docente:** Prof. Mgtr. Alberto F. Giménez Méndez  
**Universidad:** Universidad Americana

## Descripción

Conversión por rastreo sobre un frame buffer manual de Pillow. El primer
ejercicio compone una casa con líneas DDA. El segundo conecta todos los pares
de puntos de una circunferencia imaginaria mediante Bresenham y asigna el
color según la orientación de cada línea.

## Ejecución

Requiere Python 3 y Pillow. Abrir una terminal dentro de esta carpeta:

```bash
python -m pip install -r requirements.txt
python ejercicio1_casa.py
python ejercicio2_roseta.py
```

Las imágenes se guardan en el directorio desde el cual se ejecutan los scripts.

| Archivo | Dimensiones | Contenido |
| --- | --- | --- |
| casa.png | 600 × 500 | Cuerpo, techo, puerta, dos ventanas, sol y piso |
| roseta_12.png | 700 × 700 | 12 puntos y 66 líneas |
| roseta_24.png | 700 × 700 | 24 puntos y 276 líneas |
| roseta_36.png | 700 × 700 | 36 puntos y 630 líneas |
| roseta.png | 700 × 700 | Copia de la variante base N = 24 |

## Algoritmos

DDA divide las diferencias de coordenadas por el número de pasos y redondea
las posiciones acumuladas. Bresenham decide cada avance mediante un error
entero. Las firmas coinciden con las especificadas en el enunciado.
La cantidad de conexiones de cada roseta es N(N-1)/2 porque se recorre j > i.
