from math import pi
from .figuraplana import FiguraPlana

class Retangulo(FiguraPlana):
    """
    Representa um retângulo de base b altura h.
    Iniciado com canto superior direito nas coordenadas (b/2, h/2).    
    """

    def __init__(self, b:float, h:float) -> None:

        self.b = b
        self.h = h
        A = b * h
        Ix = (b * h**3) / 12
        Iy = (h * b**3) / 12
        xc = 0.0
        yc = 0.0
        Ixy = 0.0
        super().__init__(A, Ix, Iy, xc, yc, Ixy)

    def __repr__(self) -> str:
        return f"Retangulo(b={self.b}, h={self.h})"

    def __str__(self) -> str:
        txt = f"Retângulo: b= {self.b}, h= {self.h} \n"
        txt += super().__str__()
        return txt

    
class Circulo(FiguraPlana):
    """
    Representa um círculo de raio r.
    Iniciado com centro nas coordenadas (0,0) 
    """

    def __init__(self, r:float) -> None:

        self.r = r
        A = pi * r**2
        Ix = (pi * r**4) / 4
        Iy = (pi * r**4) / 4
        xc = 0.0
        yc = 0.0
        Ixy = 0.0

        super().__init__(A, Ix, Iy, xc, yc, Ixy)

    def __repr__(self) -> str:
        return f"Circulo(r={self.r})"

    def __str__(self) -> str:
        txt = f"Círculo: r= {self.r}\n"
        txt += super().__str__()
        return txt


class TrianguloRetangulo(FiguraPlana):
    """
    Representa um triângulo retângulo de base b altura h.
    Iniciado com o vértice do ângulo reto nas coordenadas (0,0) e os
    demais vértices nas coordenadas (b,0) e (0,h)."""

    def __init__(self, b:float, h:float) -> None:

        self.b = b
        self.h = h

        A = (b * h) / 2
        Ix = (b * h**3) / 12
        Iy = (h * b**3) / 12
        xc = b / 3
        yc = h / 3
        Ixy = (b**2 * h**2) / 24

        super().__init__(A, Ix, Iy, xc, yc, Ixy)

    def __repr__(self) -> str:
        return f"TrianguloRetangulo(b={self.b}, h={self.h})"

    def __str__(self) -> str:
        txt = f"Triângulo Retângulo: b= {self.b}, h= {self.h} \n"
        txt += super().__str__()
        return txt

class SemiCirculo(FiguraPlana):
    """
    Representa um semi-círculo de raio r.
    Iniciado com origem no centro do semi-círculo e ângulo de 0 a pi.
    """

    def __init__(self, r:float) -> None:

        self.r = r
        A = (pi * r**2) / 2
        Ix = (pi * r**4) / 8 - (8 * r**4) / (9 * pi)
        Iy = (pi * r**4) / 8
        xc = 0.0
        yc = 3 * r / (4 * pi)
        Ixy = 0.0

        super().__init__(A, Ix, Iy, xc, yc, Ixy) 

    def __repr__(self) -> str:
        return f"SemiCirculo(r={self.r})"

    def __str__(self) -> str:
        txt = f"Semi-Círculo: r= {self.r} \n"
        txt += super().__str__()
        return txt

class QuartoCirculo(FiguraPlana):
    """
    Representa um quarto de círculo de raio r.
    Iniciado com origem no centro do quarto de círculo e ângulo de 0 a pi/2.
    """

    def __init__(self, r:float) -> None:

        self.r = r
        A = (pi * r**2) / 4
        Ix = (pi * r**4) / 16
        Iy = (pi * r**4) / 16
        xc = 4 * r / (3 * pi)
        yc = xc
        Ixy = r**4/8
 
        super().__init__(A, Ix, Iy, xc, yc, Ixy)


    def __repr__(self) -> str:
        return f"QuartoCirculo(r={self.r})"

    def __str__(self) -> str:
        txt = f"Quarto-Círculo: r= {self.r}\n"
        txt += super().__str__()
        return txt