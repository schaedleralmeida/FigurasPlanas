import pytest
from math import sqrt, atan2, sin, cos, radians
import figurasplanas as fp


def test_figuraplana():
    ret1 = fp.FiguraPlana(48, 576, 64, 0, 0, 0)
    assert ret1.A == 48.0
    assert ret1.Ix == 576.0
    assert ret1.Iy == 64.0
    assert ret1.xc == 0.0
    assert ret1.yc == 0.0
    assert ret1.Ixy == 0.0    

    assert ret1.rx == sqrt(576/48)
    assert ret1.ry == sqrt(64/48)
    assert ret1.Io == 640.0
    assert ret1.ro == sqrt(640/48)
    assert ret1.Sx == 0.0
    assert ret1.Sy == 0.0

    assert ret1.I1 == ret1.Ix
    assert ret1.I2 == ret1.Iy
    assert ret1.theta_p == 0.0
    assert ret1.r1 == ret1.rx
    assert ret1.r2 == ret1.ry
    assert ret1.Ic == ret1.Io

    #----------------------------
    ret1.transladar(2, -6)
    assert ret1.A == 48.0
    assert ret1.xc == 2.0
    assert ret1.yc == -6.0
    assert ret1.Ix == 576.0*4
    assert ret1.Iy == 64.0*4
    assert ret1.Ixy == 2*(-6)*48.0

    assert ret1.rx == sqrt(576*4/48)
    assert ret1.ry == sqrt(64*4/48)
    assert ret1.Io == 4*640.0
    assert ret1.ro == sqrt(4*640.0/48)
    assert ret1.Sx == 2*48.0
    assert ret1.Sy == -6*48.0

    assert ret1.I1 == 576.0
    assert ret1.I2 == 64.0
    assert ret1.theta_p == 0.0
    assert ret1.r1 == sqrt(576/48)
    assert ret1.r2 == sqrt(64/48)
    assert ret1.Ic == 640.0

    #----------------------------
    xc = 2
    yc = -6
    ret2 = fp.FiguraPlana(48, 2304, 256, xc, yc, -576)
    assert vars(ret2) == pytest.approx(vars(ret1))

