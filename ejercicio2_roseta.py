"""Rosetas de todos los pares de puntos, rasterizadas con Bresenham."""
from PIL import Image
import colorsys
import math


def bresenham(pixels, x0, y0, x1, y1, color, ancho, alto):
    """Traza líneas en los ocho octantes mediante un error entero."""
    dx, dy = abs(x1 - x0), -abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    error = dx + dy
    while True:
        if 0 <= x0 < ancho and 0 <= y0 < alto:
            pixels[x0, y0] = color
        if x0 == x1 and y0 == y1:
            break
        doble_error = 2 * error
        if doble_error >= dy:
            error += dy
            x0 += sx
        if doble_error <= dx:
            error += dx
            y0 += sy


def generar_puntos_circulo(cx, cy, radio, n):
    """Devuelve n puntos separados por 2*pi/n radianes."""
    puntos = []
    for i in range(n):
        angulo = 2 * math.pi * i / n
        x = cx + round(radio * math.cos(angulo))
        y = cy + round(radio * math.sin(angulo))
        puntos.append((x, y))
    return puntos


def dibujar_roseta(pixels, puntos, ancho, alto):
    """Conecta cada par una vez; el tono depende del ángulo de la línea."""
    n = len(puntos)
    for i in range(n):
        for j in range(i + 1, n):
            x0, y0 = puntos[i]
            x1, y1 = puntos[j]
            # La orientación módulo pi asigna igual tono a líneas paralelas.
            angulo = math.atan2(y1 - y0, x1 - x0) % math.pi
            tono = angulo / math.pi
            rgb = colorsys.hsv_to_rgb(tono, 0.80, 1.0)
            color = tuple(round(componente * 255) for componente in rgb)
            bresenham(pixels, x0, y0, x1, y1, color, ancho, alto)


def main():
    ancho, alto = 700, 700
    # No se dibuja una circunferencia: solo las conexiones entre sus puntos.
    for n in (12, 24, 36):
        imagen = Image.new("RGB", (ancho, alto), "black")
        puntos = generar_puntos_circulo(350, 350, 300, n)
        dibujar_roseta(imagen.load(), puntos, ancho, alto)
        imagen.save(f"roseta_{n}.png")
        # El enunciado también solicita esta salida base con nombre fijo.
        if n == 24:
            imagen.save("roseta.png")
        print(f"Generada roseta_{n}.png: {n * (n - 1) // 2} líneas.")


if __name__ == "__main__":
    main()
