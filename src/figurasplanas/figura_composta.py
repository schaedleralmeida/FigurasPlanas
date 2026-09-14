from math import sin, cos
from figura_simples import *


class FiguraComposta(FiguraPlana):

    def __init__(self, figuras:list[FiguraPlana]) -> None:
        self.figuras = figuras

    def _calcular_propriedades_secao_composta(self, update:bool) -> None:
        self.A = sum(fig.A for fig in self.figuras)
        Sx = sum(fig.Sx for fig in self.figuras)
        Sy = sum(fig.Sy for fig in self.figuras)
        self.xc = Sx / A
        self.yc = Sy / A
        self.Ix = sum(fig.Ix + fig.A * (fig.yc - yc)**2 for fig in self.figuras)
        self.Iy = sum(fig.Iy + fig.A * (fig.xc - xc)**2 for fig in self.figuras)
        self.Ixy = sum(fig.Ixy + fig.A * (fig.xc - xc) * (fig.yc - yc) for fig in self.figuras)

        self._calcular_propriedades(update=False)


    def transladar(self, xc:float, yc:float) -> None:
        for fig in self.figuras:
            fig.transladar(xc, yc)
        self._calcular_propriedades_secao_composta(update=False)

    def rotacionar(self, theta_p:float) -> None:
        s = sin(theta_p - self.theta_p)
        c = cos(theta_p - self.theta_p)

        for fig in self.figuras:
            rx = fig.xc - self.xc
            ry = fig.yc - self.yc
            xc_fig = self.xc + c * rx - s * ry
            yc_fig = self.yc + s * rx + c * ry
            theta_p_fig = fig.theta_p + (theta_p - self.theta_p)
            fig.transladar(xc_fig, yc_fig)
            fig.rotacionar(theta_p_fig)

        self._calcular_propriedades_secao_composta(update=False)

    def __repr__(self) -> str:
        return f"FiguraComposta(figuras={self.figuras})"

    def __str__(self) -> str:
        txt = "Figura Composta:\n"
        for fig in self.figuras:
            txt += f"  {fig}\n"
        txt += super().__str__()
        return txt