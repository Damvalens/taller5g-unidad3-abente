
from PIL import Image
import math


def dda(pixels, x0, y0, x1, y1, color, ancho, alto):

    dx, dy = x1 - x0, y1 - y0
    pasos = max(abs(dx), abs(dy))
    if pasos == 0:
        if 0 <= x0 < ancho and 0 <= y0 < alto:
            pixels[x0, y0] = color
        return
    incremento_x, incremento_y = dx / pasos, dy / pasos
    x, y = float(x0), float(y0)
    for _ in range(pasos + 1):
        px, py = round(x), round(y)
        if 0 <= px < ancho and 0 <= py < alto:
            pixels[px, py] = color
        x += incremento_x
        y += incremento_y


def dibujar_rectangulo(pixels, x0, y0, x1, y1, color, ancho, alto):

    dda(pixels, x0, y0, x1, y0, color, ancho, alto)
    dda(pixels, x1, y0, x1, y1, color, ancho, alto)
    dda(pixels, x1, y1, x0, y1, color, ancho, alto)
    dda(pixels, x0, y1, x0, y0, color, ancho, alto)


def dibujar_triangulo(pixels, p1, p2, p3, color, ancho, alto):

    for inicio, fin in [(p1, p2), (p2, p3), (p3, p1)]:
        dda(pixels, *inicio, *fin, color, ancho, alto)


def dibujar_puerta(pixels, x0, y0, x1, y1, color, ancho, alto):

    dibujar_rectangulo(pixels, x0, y0, x1, y1, color, ancho, alto)


def dibujar_ventana(pixels, x, y, lado, color, ancho, alto):
 
    dibujar_rectangulo(pixels, x, y, x + lado, y + lado, color, ancho, alto)


def dibujar_sol(pixels, cx, cy, radio, n_rayos, color, ancho, alto):

    for i in range(n_rayos):
        angulo = 2 * math.pi * i / n_rayos
        x = cx + round(radio * math.cos(angulo))
        y = cy + round(radio * math.sin(angulo))
        dda(pixels, cx, cy, x, y, color, ancho, alto)


def dibujar_piso(pixels, y, color, ancho, alto):

    dda(pixels, 0, y, ancho - 1, y, color, ancho, alto)


def main():
    ancho, alto = 600, 500
    imagen = Image.new("RGB", (ancho, alto), (200, 230, 255))
    pixels = imagen.load()

    dibujar_rectangulo(pixels, 150, 240, 450, 420, (35, 75, 180), ancho, alto)
    dibujar_triangulo(pixels, (125, 240), (300, 110), (475, 240),
                     (195, 40, 45), ancho, alto)
    dibujar_puerta(pixels, 270, 325, 330, 420, (130, 75, 30), ancho, alto)
    dibujar_ventana(pixels, 185, 275, 55, (0, 140, 150), ancho, alto)
    dibujar_ventana(pixels, 360, 275, 55, (0, 140, 150), ancho, alto)
    dibujar_sol(pixels, 510, 80, 45, 12, (235, 150, 0), ancho, alto)
    dibujar_piso(pixels, 420, (45, 120, 55), ancho, alto)
    imagen.save("casa.png")
    print("Generada casa.png (600 x 500 píxeles).")


if __name__ == "__main__":
    main()
