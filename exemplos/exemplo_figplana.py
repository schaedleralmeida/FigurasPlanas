from math import degrees, radians
import figurasplanas as fp

b = 9
h = 6

#%%--------------------
fig1 = fp.FiguraPlana(A=b*h, Ix=b*h**3/12, Iy=h*b**3/12, Ixy=0, xc=0, yc=0)
print("\n Propriedades da figura 1:")
print(fig1)

print(f"Ângulo dos eixos principais: {degrees(fig1.theta_p)}º")


fig1.transladar(xc=b/2, yc=h/2)
print("\n Propriedades da figura 1 após  translação:")
print(fig1)
print(f"Ângulo dos eixos principais: {degrees(fig1.theta_p)}º")

#%%--------------------

#cria a figura
fig2 = fp.FiguraPlana(A=b*h/2, Ix=b*h**3/12, Iy=h*b**3/12, Ixy=(b*h)**2/24, xc=b/3, yc=h/3)

#imprime as propriedades da figura
print("\n Propriedades da figura 2:")
print(fig2)
print(f"Ângulo dos eixos principais: {degrees(fig2.theta_p)}º")







