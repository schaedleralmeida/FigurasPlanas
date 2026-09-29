'''
Resolve os exemplos 10.6, 10,8 e 10.9 do livro "Estática - Mecânica para Engenharia" de R.C. Hibbeler (10a edição, Pearson, 2005).

'''


#%%
from math import pi
import figurasplanas as fp

fig = fp.FiguraComposta()
print("figura criada")
print(fig)

#%%
parte_A = fp.Retangulo(100, 300)
parte_A.transladar(-250, 200)
fig.adiciona(parte_A)
print("\n parte A adicionada")
print(fig)

#%%
parte_B = fp.Retangulo(600, 100)
fig.adiciona(parte_B)
print("\n parte B adicionada")
print(fig)

#%%
parte_C = fp.Retangulo(100, 300)
parte_C.transladar(250, -200)
fig.adiciona(parte_C)
print("\n parte C adicionada")
print(fig)

#%%
print("\nPropriedades da seção composta:")
print(fig)

print(f"\n theta_p = {fig.theta_p*180/pi:.2f} graus")


print("\nPropriedades das partes da seção composta:")
for i, parte in enumerate(fig.partes):
    print(f"Parte {i}: {parte}")

