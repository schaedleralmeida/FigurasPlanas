#%%
from math import pi
import figurasplanas as fp

fig = fp.FiguraComposta()
print("figura criada")
print(fig)

#%%
parte1 = fp.Retangulo(6, 10)
parte1.transladar(3, 5)
fig.adiciona(parte1)
print("\n parte 1 adicionada")
print(fig)

#%%
parte2 = fp.Circulo(2)
parte2.transladar(3, 4)
fig.adiciona(parte2, coef=-1.0)
print("\n parte 2 adicionada")
print(fig)

#%%
parte3 = fp.TrianguloRetangulo(3, 6)

parte3.rotacionar(-pi)
parte3.transladar(6, 10)
fig.adiciona(parte3, coef=-1.0)
print("\n parte 3 adicionada")
print(fig)

#%%
print(fig)