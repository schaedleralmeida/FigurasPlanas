#%%
from math import pi
import figurasplanas as fp


fig = fp.FiguraComposta()

#%%
parte1 = fp.Retangulo(6, 10)
parte1.transladar(3, 5)
fig.add(parte1)

#%%
parte2 = fp.Circulo(2)
parte2.transladar(3, 4)
fig.add(parte2, coef=-1.0)


#%%
parte3 = fp.TrianguloRetangulo(3, 6)
parte3.transladar(6-parte3.xc, 10-parte3.yc)
parte3.rotacionar(parte3.theta_p -pi)
fig.add(parte3, coef=-1.0)

#%%
print(fig)