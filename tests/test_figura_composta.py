import pytest
from math import sqrt, atan2, sin, cos, radians
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