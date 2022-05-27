import matplotlib.pyplot as plt
import numpy as np
from math import *

# Calculo Robo:
# modelo: small size
raioRobo = 0.09 # metros
raioIntercep = raioRobo + (1/3*raioRobo) + 0.0215
aceleMax = 2 # m/s^s
veloMax = 3 # m/s
posRoboX = float(input("Defina a posição inicial do robo em X no campo (m): "))
posRoboY = float(input("Defina a posição inicial do robo em Y no campo (m): "))

# Dados da bola:
v0B = 0.64 # m/s
posBolaX = 1
posBolaY = 0.5
tempoTot = 0
encontrou = False
distRoboBola = sqrt(((posBolaX - posRoboX)**2) + ((posBolaY - posRoboY)**2))
print(distRoboBola)

# Encontrar a bola:
while tempoTot <= 20:
    yB = -0.008*(tempoTot**2) + 0.4*tempoTot + 0.5
    xB = -0.005*(tempoTot**2) + 0.5*tempoTot + 1

    posBolaY = yB
    posBolaX = xB
    distRoboBola = sqrt(((posBolaX - posRoboX)**2) + ((posBolaY - posRoboY)**2))

    if tempoTot != 0:
        acelePrecisa = (2*distRoboBola)/(tempoTot**2)
        print("\nacele teste =",acelePrecisa)
        print("tempotot =%f\n"%tempoTot)
        veloPrecisa = acelePrecisa*tempoTot
        if acelePrecisa > aceleMax or veloPrecisa > veloMax:
            pass
        else:
            aceleRobo = acelePrecisa
            veloRobo = veloPrecisa
            direcao = atan((posBolaY - posRoboY)/(posBolaX - posRoboX))
            encontrou = True
            tempoEncontro = tempoTot
            break

    tempoTot += 0.02

print(aceleRobo)
print(veloRobo)
print(direcao*180/pi)
print(encontrou)
print(tempoEncontro)



# Criar figura e eixos
fig, ax = plt.subplots()

######## Trajetória no campo ###########
x = np.linspace(1, 9, 1000)
ybola = -0.0309*(x**2) + 0.9215*x - 0.4366
xpLimitebola = -0.005*(tempoEncontro**2) + 0.5*tempoEncontro + 1
rx = np.linspace(posRoboX, xpLimitebola, 1000)
yrobo = tan(direcao)*(rx - posRoboX) + posRoboY
ax.plot(x,ybola, label='Bola')
ax.plot(rx,yrobo, label='Robo')
#Personalizações do Gráfico
plt.xlabel("Posição X (m)")
plt.ylabel("Posição Y (m)")
plt.title("Trajetoria Campo")
plt.legend()

plt.show()

###### Gráficos Posições Y/Tempo ##########
fig, ax = plt.subplots()
tempo = np.linspace(0, tempoEncontro, 1000)
ypbola = -0.008*(tempo**2) + 0.4*tempo + 0.5
yprobo = posRoboY + sin(direcao)*aceleRobo*(tempo**2)/2
ax.plot(tempo, ypbola, label = 'Bola')
ax.plot(tempo, yprobo, label = 'Robo')

#Personalizações do Gráfico
plt.xlabel("Tempo (s)")
plt.ylabel("Posição Y (m)")
plt.title("Posição Y / Tempo")
plt.grid()
plt.legend()

# Printar o gráfico
plt.show()

###### Gráficos Posições X/Tempo ##########
fig, ax = plt.subplots()
tempo = np.linspace(0, tempoEncontro, 1000)
xpbola = -0.005*(tempo**2) + 0.5*tempo + 1
xprobo = posRoboX + cos(direcao)*aceleRobo*(tempo**2)/2
ax.plot(tempo, xpbola, label = 'Bola')
ax.plot(tempo, xprobo, label = 'Robo')

#Personalizações do Gráfico
plt.xlabel("Tempo (s)")
plt.ylabel("Posição X (m)")
plt.title("Posição X / Tempo")
plt.grid()
plt.legend()

# Printar o gráfico
plt.show()

###### Gráficos Velocidades X/Tempo ##########
fig, ax = plt.subplots()
tempo = np.linspace(0, tempoEncontro, 1000)
xvbola = -0.010*tempo + 0.5
xvrobo = cos(direcao)*aceleRobo*(tempo)
ax.plot(tempo, xvbola, label = 'Bola')
ax.plot(tempo, xvrobo, label = 'Robo')

#Personalizações do Gráfico
plt.xlabel("Tempo (s)")
plt.ylabel("Velocidade X (m/s)")
plt.title("Velocidade X / Tempo")
plt.grid()
plt.legend()

# Printar o gráfico
plt.show()

###### Gráficos Velocidades Y/Tempo ##########
fig, ax = plt.subplots()
tempo = np.linspace(0, tempoEncontro, 1000)
yvbola = -0.016*tempo + 0.4
yvrobo = sin(direcao)*aceleRobo*(tempo)
ax.plot(tempo, yvbola, label = 'Bola')
ax.plot(tempo, yvrobo, label = 'Robo')

#Personalizações do Gráfico
plt.xlabel("Tempo (s)")
plt.ylabel("Velocidade Y (m/s)")
plt.title("Velocidade Y / Tempo")
plt.grid()
plt.legend()

# Printar o gráfico
plt.show()

###### Gráficos Aceleração X/Tempo ##########
fig, ax = plt.subplots()
tempo = np.linspace(0, tempoEncontro, 1000)
xabola = -0.010*(tempo**0)
xarobo = cos(direcao)*aceleRobo*(tempo**0)
plt.plot(tempo, xabola, label = 'Bola')
plt.plot(tempo, xarobo, label = 'Robo')

#Personalizações do Gráfico
plt.xlabel("Tempo (s)")
plt.ylabel("Aceleração X (m/s^2)")
plt.title("Aceleração X / Tempo")
plt.grid()
plt.legend()

# Printar o gráfico
plt.show()

###### Gráficos Aceleração Y/Tempo ##########
fig, ax = plt.subplots()
tempo = np.linspace(0, tempoEncontro, 1000)
yabola = -0.016*(tempo**0)
xarobo = sin(direcao)*aceleRobo*(tempo**0)
plt.plot(tempo, xabola, label = 'Bola')
plt.plot(tempo, xarobo, label = 'Robo')

#Personalizações do Gráfico
plt.xlabel("Tempo (s)")
plt.ylabel("Aceleração Y (m/s^2)")
plt.title("Aceleração Y / Tempo")
plt.grid()
plt.legend()

# Printar o gráfico
plt.show()