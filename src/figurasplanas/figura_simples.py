from math import pi
from .figuraplana import FiguraPlana

class Retangulo(FiguraPlana):
    """
    Representa um retângulo de base b altura h.
    Para xc=0 e yc=0, o retângulo é centrado na origem do sistema de coordenadas e o eixo x é paralelo à base.    
    """

    def __init__(self, b:float, h:float, xc:float=0.0, yc:float=0.0, theta:float=0.0) -> None:

        self.b = b
        self.h = h
        A = b * h
        Ix = (b * h**3) / 12
        Iy = (h * b**3) / 12
        Ixy = 0.0

        super().__init__(A, Ix, Iy, xc, yc, Ixy)

        if theta != 0.0:
            self.rotacionar(self.theta_p + theta)

    def __repr__(self) -> str:
        return f"Retangulo(b={self.b}, h={self.h}, xc={self.xc}, yc={self.yc}, theta={self.theta_p})"

    def __str__(self) -> str:
        txt = f"Retângulo: b= {self.b}, h= {self.h}, xc= {self.xc}, yc= {self.yc}, theta= {self.theta_p}\n"
        txt += super().__str__()
        return txt

    
class Circulo(FiguraPlana):
    """
    Representa um círculo de raio r.
    Para xc=0 e yc=0, o círculo é centrado na origem do sistema de coordenadas."""

    def __init__(self, r:float, xc:float=0.0, yc:float=0.0) -> None:

        self.r = r
        A = pi * r**2
        Ix = (pi * r**4) / 4
        Iy = (pi * r**4) / 4
        Ixy = 0.0

        super().__init__(A, Ix, Iy, xc, yc, Ixy)

    def __repr__(self) -> str:
        return f"Circulo(r={self.r}, xc={self.xc}, yc={self.yc})"

    def __str__(self) -> str:
        txt = f"Círculo: r= {self.r}, xc= {self.xc}, yc= {self.yc}\n"
        txt += super().__str__()
        return txt


class TrianguloRetangulo(FiguraPlana):
    """
    Representa um triângulo retângulo de base b altura h. Para xc=None e yc=None, e theta=0, a origem do sistema de coordenadas fica no vérice do ângulo reto e o eixo x é paralelo à base."""

    def __init__(self, b:float, h:float, xc:None|float=None, yc:None|float=None, theta:float=0.0) -> None:

        self.b = b
        self.h = h

        A = (b * h) / 2
        Ix = (b * h**3) / 36
        Iy = (h * b**3) / 36
        Ixy = (b**2 * h**2) / 72
        xc = b / 3 if xc is None else xc
        yc = h / 3 if yc is None else yc

        super().__init__(A, Ix, Iy, xc, yc, Ixy)

        self.theta_p0 = self.theta_p

        if theta != 0.0:
            self.rotacionar(self.theta_p + theta)

    def __repr__(self) -> str:
        return f"TrianguloRetangulo(b={self.b}, h={self.h}, xc={self.xc}, yc={self.yc}, theta={self.theta_p - self.theta_p0})"

    def __str__(self) -> str:
        txt = f"Triângulo Retângulo: b= {self.b}, h= {self.h}, xc= {self.xc}, yc= {self.yc}, theta= {self.theta_p}\n"
        txt += super().__str__()
        return txt

class SemiCirculo(FiguraPlana):
    """ Representa um semi-círculo de raio r. Para xc=0 e yc=0, a origem do sistema de coordenadas fica no centro do semi-círculo e o eixo x é paralelo à base."""

    def __init__(self, r:float, xc:float=0.0, yc:float=0.0, theta:float=0.0) -> None:

        self.r = r
        A = (pi * r**2) / 2
        Ix = (pi * r**4) / 8 - (8 * r**4) / (9 * pi)
        Iy = (pi * r**4) / 8
        Ixy = 0.0

        super().__init__(A, Ix, Iy, xc, yc, Ixy)
        if theta != 0.0:
            self.rotacionar(self.theta_p + theta)

    def __repr__(self) -> str:
        return f"SemiCirculo(r={self.r}, xc={self.xc}, yc={self.yc}, theta={self.theta_p})"

    def __str__(self) -> str:
        txt = f"Semi-Círculo: r= {self.r}, xc= {self.xc}, yc= {self.yc}\n"
        txt += super().__str__()
        return txt

class QuartoCirculo(FiguraPlana):
    """ Representa um quarto de círculo de raio r. Para xc=0 e yc=0, a origem do sistema de coordenadas fica no centro do quarto de círculo e o eixo x é paralelo à base."""

    def __init__(self, r:float, xc:float=0.0, yc:float=0.0, theta:float=0.0) -> None:

        self.r = r
        A = (pi * r**2) / 4
        Ix = (pi * r**4) / 16 - (8 * r**4) / (9 * pi)
        Iy = (pi * r**4) / 16 - (8 * r**4) / (9 * pi)
        Ixy = 0.0

        super().__init__(A, Ix, Iy, xc, yc, Ixy)

        self.theta_p0 = self.theta_p

        if theta != 0.0:
            self.rotacionar(theta + self.theta_p)

    def __repr__(self) -> str:
        return f"QuartoCirculo(r={self.r}, xc={self.xc}, yc={self.yc}, theta={self.theta_p - self.theta_p0})"

    def __str__(self) -> str:
        txt = f"Quarto-Círculo: r= {self.r}, xc= {self.xc}, yc= {self.yc}\n"
        txt += super().__str__()
        return txt