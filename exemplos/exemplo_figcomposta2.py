"""
Exemplo de figura composta formulado e resolvido pelo Prof. Felipe M. Quevedo (DECIV/UFRGS).
"""

#%%
from math import pi
import figurasplanas as fp

fig = fp.FiguraComposta()
print("figura criada")
print(fig)

#%%

b = 120
h1 = 80
h2 = 60
r = 40

#%%
parte1 = fp.SemiCirculo(b/2)
parte1.transladar(b/2, h1+h2)
fig.adiciona(parte1)

#%%
parte2 = fp.Retangulo(b, h1)
parte2.transladar(b/2, h2+h1/2)
fig.adiciona(parte2)

#%%
parte3 = fp.TrianguloRetangulo(h2, b)
parte3.rotacionar(-pi/2)
parte3.transladar(0, h2)
fig.adiciona(parte3)

#%%
parte4 = fp.Circulo(r)
parte4.transladar(b/2, h1+h2)
fig.adiciona(parte4, coef= -1)

#%%
print("\nPropriedades da seção composta:")
print(fig)

print(f"\n theta_p = {fig.theta_p*180/pi:.2f} graus")

print("\nPropriedades das partes da seção composta:")
for i, parte in enumerate(fig.partes):
    print(f"Parte {i}: {parte}")

# %%
