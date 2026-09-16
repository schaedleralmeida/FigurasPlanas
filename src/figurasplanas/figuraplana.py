from math import atan2, pi, sqrt, sin, cos


class FiguraPlana:
    """Representa uma figura plana genérica por suas propriedades geométricas.

    A classe armazena a área, os momentos de inércia em relação aos
    eixos x e y, o produto de inércia Ixy, e a posição do centroide (xc, yc).
    A partir desses dados, ela calcula também os momentos principais, o ângulo
    principal theta_p e os raios de giração associados.

    Atributos:
        A (float): área.
        Ix (float): momento de inércia em relação ao eixo x global.
        Iy (float): momento de inércia em relação ao eixo y global.
        Ixy (float): produto de inércia da seção em relação aos eixos x e y.
        xc (float): coordenada x do centroide.
        yc (float): coordenada y do centroide.
        Io (float): momento polar de inércia para origem dos eixos x-y.
        Sx, Sy (float): momentos estáticos em relação aos eixos x e y.
        rx, ry (float): raios de giração em relação aos eixos x e y.
        ro (float): raio de giração polar para origem dos eixos x-y.
        Ic (float): momento de inércia polar em relação ao centroide.
        I1, I2 (float): momentos principais de inércia.
        theta_p (float): ângulo entre x-y e os eixos principais.
        r1, r2 (float): raios de giração principais.

    Métodos:
        transladar(xc, yc): atualiza a posição do centroide e recalcula as
            propriedades.
        rotacionar(theta_p): redefine o ângulo dos eixos principais e recalcula
            as propriedades.
    """
    
    def __init__(self, A:float, Ix:float, Iy:float, xc:float, yc:float, Ixy:float)-> None: 
        self.A = A
        self.Ix = Ix
        self.Iy = Iy
        self.Ixy = Ixy
        self.xc = xc
        self.yc = yc

        if any([value < 0 for value in [A, Ix, Iy]]):
            raise ValueError("Área e momentos de inércia devem ser não-negativos.")
        if Ix*Iy < Ixy**2:
            raise ValueError("Há inconsistência nos valores de Ix, Iy, Ixy.")
        
        self._eixos_principais_centrais()
        self._calcular_propriedades(update=False)


    def _eixos_principais_centrais(self) -> None:
        self.Ix_a = self.Ix - self.yc**2 * self.A
        self.Iy_a = self.Iy - self.xc**2 * self.A
        self.Ixy_a = self.Ixy - self.xc * self.yc * self.A

        self.I1 = (self.Ix_a + self.Iy_a) / 2 + sqrt( ((self.Ix_a - self.Iy_a) / 2)**2 + self.Ixy_a**2 )
        self.I2 = (self.Ix_a + self.Iy_a) / 2 - sqrt( ((self.Ix_a - self.Iy_a) / 2)**2 + self.Ixy_a**2 )
        self.theta_p = 0.5 * atan2(2 * self.Ixy_a, self.Ix_a - self.Iy_a)
        if self.I2 <=0:
            raise ValueError("Há inconsistência nos valores de Ix, Iy, Ixy que resultam em I2 negativo.")

        self.r1 = sqrt( self.I1 / self.A )
        self.r2 = sqrt( self.I2 / self.A )
        self.Ic = self.I1 + self.I2


    def _calcular_propriedades(self,update:bool) -> None:

        if update:
            self.Ix = self.Ix_a + self.yc**2 * self.A
            self.Iy = self.Iy_a + self.xc**2 * self.A
            self.Ixy = self.Ixy_a + self.xc * self.yc * self.A

        self.Io = self.Ix + self.Iy
        self.Sx = self.xc * self.A
        self.Sy = self.yc * self.A
        self.rx = sqrt( self.Ix / self.A )
        self.ry = sqrt( self.Iy / self.A )
        self.ro = sqrt( self.Io / self.A )

    def transladar(self, xc:float, yc:float) -> None:
        """Translada a figura plana para uma nova posição do centroide (xc, yc)."""
        self.xc = xc
        self.yc = yc
        self._calcular_propriedades(update=True)


    def rotacionar(self, theta_p:float) -> None:
        """Rotação em torno do centroide da figura plana até a posição theta_p dos eixos principais. O ângulo theta_p é medido em radianos."""
        self.theta_p = theta_p
        self.Ix_a = (self.I1 + self.I2 ) / 2 + (self.I1 - self.I2) / 2 * cos(2 * self.theta_p)
        self.Iy_a = (self.I1 + self.I2 ) / 2 - (self.I1 - self.I2) / 2 * cos(2 * self.theta_p)
        self.Ixy_a = (self.I1 - self.I2) / 2 * sin(2 * self.theta_p)

        self._calcular_propriedades(update=False)

    def __repr__(self) -> str:
        return f"FiguraPlana(A={self.A}, Ix={self.Ix}, Iy={self.Iy}, Ixy={self.Ixy}, xc={self.xc}, yc={self.yc})"
    
    def __str__(self) -> str:
        def formatar_linha(*propriedades: tuple[str, float]) -> str:
            return ", ".join(
                f"{nome:>7}: {valor:>12.4e}"
                for nome, valor in propriedades
            )

        return (
            formatar_linha(
                ("A", self.A), ("Ix", self.Ix), ("Iy", self.Iy),
                ("Ixy", self.Ixy), ("xc", self.xc), ("yc", self.yc),
            ) + "\n" +
            formatar_linha(
                ("Io", self.Io), ("Sx", self.Sx), ("Sy", self.Sy),
                ("rx", self.rx), ("ry", self.ry), ("ro", self.ro),
            ) + "\n" +
            formatar_linha(
                ("I1", self.I1), ("I2", self.I2),
                ("theta_p", self.theta_p), ("Ic", self.Ic),
                ("r1", self.r1), ("r2", self.r2),
            )
        )