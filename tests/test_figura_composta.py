import pytest
from math import sqrt, atan2, sin, cos, radians, pi
import figurasplanas as fp


def test_figura_composta1():
    """ 
    Teste da figura composta dosexemplos 10.6, 10,8 e 10.9 do livro "Estática - Mecânica para Engenharia" de R.C. Hibbeler (10a edição, Pearson, 2005)
    """
    fig = fp.FiguraComposta()
    parte_A = fp.Retangulo(100, 300)
    parte_A.transladar(-250, 200)
    fig.adiciona(parte_A)

    parte_B = fp.Retangulo(600, 100)
    fig.adiciona(parte_B)

    parte_C = fp.Retangulo(100, 300)
    parte_C.transladar(250, -200)
    fig.adiciona(parte_C)

    assert fig.Ix == pytest.approx(2.9e9, rel=1e-6)
    assert fig.Iy == pytest.approx(5.6e9, rel=1e-6)
    assert fig.Ixy == pytest.approx(-3.0e9, rel=1e-6)
    assert fig.I1 == pytest.approx(7.54e9, rel=1e-3)
    assert fig.I2 == pytest.approx(0.96e9, rel=1e-3)
    assert fig.theta_p == pytest.approx(radians(57.1), rel=1e-3)


def test_figura_composta2():
    """
    Teste da figura composta formulado e resolvido pelo Prof. Felipe M. Quevedo (DECIV/UFRGS).
    """

    fig = fp.FiguraComposta()

    b = 120
    h1 = 80
    h2 = 60
    r = 40

    parte1 = fp.SemiCirculo(b/2)
    parte1.transladar(b/2, h1+h2)
    fig.adiciona(parte1)

    parte2 = fp.Retangulo(b, h1)
    parte2.transladar(b/2, h2+h1/2)
    fig.adiciona(parte2)

    parte3 = fp.TrianguloRetangulo(h2, b)
    parte3.rotacionar(-pi/2)
    parte3.transladar(0, h2)
    fig.adiciona(parte3)

    parte4 = fp.Circulo(r)
    parte4.transladar(b/2, h1+h2)
    fig.adiciona(parte4, coef= -1)

    assert fig.A == pytest.approx(13828.31, rel=1e-2)
    assert fig.xc == pytest.approx(54.77, rel=1e-2)
    assert fig.yc == pytest.approx(96.74, rel=1e-2)

    assert fig.Ix == pytest.approx(16.32e7, rel=1e-2)
    assert fig.Iy == pytest.approx(6.0e7, rel=1e-2)
    assert fig.Ixy == pytest.approx(7.79e7, rel=1e-2)

    assert fig.theta_p == pytest.approx(radians(-15.7), rel=1e-2)
    assert fig.I1 == pytest.approx(3.56e7, rel=1e-2)
    assert fig.I2 == pytest.approx(1.71e7, rel=1e-2)
