from math import sin, cos
from .figura_simples import *


class FiguraComposta(FiguraPlana):
 
    def __init__(self) -> None:
        self.partes = []
        self.coef = []
        #self._calcular_propriedades_secao_composta()


    def add(self, figura:FiguraPlana, coef=1.0) -> None:
        self.partes.append(figura)
        self.coef.append(coef)
        self._calcular_propriedades_secao_composta()

    def remove(self, figura:FiguraPlana) -> None:
        if figura in self.partes:
            index = self.partes.index(figura)
            del self.partes[index]
            del self.coef[index]
            self._calcular_propriedades_secao_composta()

    def _calcular_propriedades_secao_composta(self) -> None:

        A = Sx = Sy = Ix = Iy = Ixy = 0.0
        for fig, c in zip(self.partes, self.coef):
            A += c * fig.A
            Sx += c * fig.Sx
            Sy += c * fig.Sy
            Ix += c * fig.Ix
            Iy += c * fig.Iy
            Ixy += c * fig.Ixy

        xc = Sx / A if A != 0 else 0.0
        yc = Sy / A if A != 0 else 0.0

        self.A = A
        self.xc = xc
        self.yc = yc
        self.Ix = Ix
        self.Iy = Iy
        self.Ixy = Ixy

        self._eixos_principais_centrais()
        self._calcular_propriedades(update=False)


    def transladar(self, xc:float, yc:float) -> None:
        for fig in self.partes:
            fig.transladar(xc, yc)
        self._calcular_propriedades_secao_composta()

    def rotacionar(self, theta_p:float) -> None:
        dtheta = theta_p - self.theta_p

        s = sin(dtheta)
        c = cos(dtheta)

        for fig in self.partes:
            rx = fig.xc - self.xc
            ry = fig.yc - self.yc
            xc_fig = self.xc + c * rx - s * ry
            yc_fig = self.yc + s * rx + c * ry
            theta_p_fig = fig.theta_p + (dtheta)
            fig.transladar(xc_fig, yc_fig)
            fig.rotacionar(theta_p_fig)

        self._calcular_propriedades_secao_composta()

    def __repr__(self) -> str:
        return f"FiguraComposta(partes={self.partes.__repr__()})"

    def __str__(self) -> str:
        txt = "Figura Composta:\n"
        for fig in self.partes:
            txt += f"  {fig.__repr__()}\n"
        txt += super().__str__()
        return txt