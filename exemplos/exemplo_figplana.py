#%%
from math import degrees, radians
import figurasplanas as fp

b = 9
h = 6

#%%--------------------
fig1 = fp.FiguraPlana(A=b*h, Ix=b*h**3/12, Iy=h*b**3/12, Ixy=0, xc=0, yc=0)
print("\n Propriedades da figura 1:")
print(fig1)

fig1.ajustar_posição(xc=h/2, yc=b/2, theta_p=radians(0))
print("\n Propriedades da figura 1 após ajuste de posição:")
print(fig1)

print("\n Diferença entre as propriedades da figura 1 movida para a posição final e a figura criada na posição final:")
fig1_pfinal = fp.FiguraPlana(A=b*h, Ix=h*b**3/3, Iy=b*h**3/3, Ixy=(b/2)*(h/2)*b*h, xc=h/2, yc=b/2)
for var in vars(fig1_pfinal):
    print(f"{var}: {getattr(fig1_pfinal, var) - getattr(fig1, var)}")

#%%--------------------

#cria a figura
fig2 = fp.FiguraPlana(A=b*h/2, Ix=b*h**3/12, Iy=h*b**3/12, Ixy=(b*h)**2/24, xc=b/3, yc=h/3)

#imprime as propriedades da figura
print("\n Propriedades da figura 2:")
print(fig2)
print(f"Ângulo dos eixos principais: {degrees(fig2.theta_p)}º")






