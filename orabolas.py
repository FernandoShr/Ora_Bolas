from operator import ne
from matplotlib import image
import matplotlib.pyplot as plt
import numpy as np
from math import *
from tkinter import *
from functools import partial
from tkinter import messagebox


janela = Tk()
janela.geometry("700x350")
janela.title("Ora Bolas")

janela.configure(bg='#9FFFF6')

t1 = Label(janela, text="Posição inicial do Robô em X:", font=("Times New Roman",13), bg='#9FFFF6')
t1.place(relx=0.48, rely=0.02, anchor=NE)
posRoboX = Entry(janela, width=20, font=("Times New Roman", 13))
posRoboX.place(relx=0.5, rely=0.02, anchor=NW)

t2 = Label(janela, text="Posição inicial do Robô em Y:", font=("Times New Roman",13), bg='#9FFFF6')
t2.place(relx=0.48, rely=0.1, anchor=NE)
posRoboY = Entry(janela, width=20, font=("Times New Roman", 13))
posRoboY.place(relx=0.5, rely=0.1, anchor=NW)


# Calculo Robo:
# modelo: small size
raioRobo = 0.09 # metros
raioIntercep = raioRobo + (1/3*raioRobo) + 0.0215
aceleMax = 2 # m/s^s
veloMax = 3 # m/s
#posRoboX = float(input("Defina a posição inicial do robo em X no campo (m): "))
#posRoboY = float(input("Defina a posição inicial do robo em Y no campo (m): "))

# Dados da bola:
v0B = 0.64 # m/s
posBolaX = 1
posBolaY = 0.5
tempoTot = 0
encontrou = False
#distRoboBola = sqrt(((posBolaX - posRoboX)**2) + ((posBolaY - posRoboY)**2))
#print(distRoboBola)

# Encontrar a bola:
# while tempoTot <= 20:
#     yB = -0.008*(tempoTot**2) + 0.4*tempoTot + 0.5
#     xB = -0.005*(tempoTot**2) + 0.5*tempoTot + 1

#     posBolaY = yB
#     posBolaX = xB
#     distRoboBola = sqrt(((posBolaX - posRoboX)**2) + ((posBolaY - posRoboY)**2))

#     if tempoTot != 0:
#         acelePrecisa = (2*distRoboBola)/(tempoTot**2)
#         print("\nacele teste =",acelePrecisa)
#         print("tempotot =%f\n"%tempoTot)
#         veloPrecisa = acelePrecisa*tempoTot
#         if acelePrecisa > aceleMax or veloPrecisa > veloMax:
#             pass
#         else:
#             aceleRobo = acelePrecisa
#             veloRobo = veloPrecisa
#             direcao = atan((posBolaY - posRoboY)/(posBolaX - posRoboX))
#             encontrou = True
#             tempoEncontro = tempoTot
#             break

#     tempoTot += 0.02

# print(aceleRobo)
# print(veloRobo)
# print(direcao*180/pi)
# print(encontrou)
# print(tempoEncontro)


def msg():
    aviso = messagebox.showinfo('Aviso', 'Valor Inválido, Robô fora de campo!\nPor favor, selecione um valor entre 0 a 9 para X e entre 0 a 6 para Y.')


######## Trajetória no campo ###########
def graphTrajetoCampo(posRoboX, posRoboY):
    if posRoboX < 0 or posRoboX > 9:
        msg()
        return
    elif posRoboY < 0 or posRoboY > 6:
        msg();
        return
    else:
        pass

    raioRobo = 0.09 # metros
    raioIntercep = raioRobo + (1/3*raioRobo) + 0.0215
    aceleMax = 2 # m/s^s
    veloMax = 3 # m/s
    #posRoboX = float(input("Defina a posição inicial do robo em X no campo (m): "))
    #posRoboY = float(input("Defina a posição inicial do robo em Y no campo (m): "))

    # Dados da bola:
    v0B = 0.64 # m/s
    posBolaX = 1
    posBolaY = 0.5
    tempoTot = 0
    encontrou = False
    distRoboBola = sqrt(((posBolaX - posRoboX)**2) + ((posBolaY - posRoboY)**2))
    #print(distRoboBola)

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

    # Criar figura e eixos
    fig, ax = plt.subplots()
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
def graphPosY(posRoboX, posRoboY):
    if posRoboX < 0 or posRoboX > 9:
        msg()
        return
    elif posRoboY < 0 or posRoboY > 6:
        msg();
        return
    else:
        pass 
    raioRobo = 0.09 # metros
    raioIntercep = raioRobo + (1/3*raioRobo) + 0.0215
    aceleMax = 2 # m/s^s
    veloMax = 3 # m/s
    #posRoboX = float(input("Defina a posição inicial do robo em X no campo (m): "))
    #posRoboY = float(input("Defina a posição inicial do robo em Y no campo (m): "))

    # Dados da bola:
    v0B = 0.64 # m/s
    posBolaX = 1
    posBolaY = 0.5
    tempoTot = 0
    encontrou = False
    distRoboBola = sqrt(((posBolaX - posRoboX)**2) + ((posBolaY - posRoboY)**2))
    #print(distRoboBola)

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

    # if posRoboY > -0.0309*(posRoboX**2) + 0.9215*posRoboX - 0.4366:
    #     aceleRoboY = - abs(sin(direcao))*aceleRobo
    # else:
    #     aceleRoboY = abs(sin(direcao))*aceleRobo

    ypbola = -0.008*(tempoEncontro**2) + 0.4*tempoEncontro + 0.5
    if posRoboY > ypbola:
        aceleRoboY = - abs(sin(direcao))*aceleRobo
    else:
        aceleRoboY = abs(sin(direcao))*aceleRobo

    # aceleRoboY = sin(direcao)*aceleRobo
    fig, ax = plt.subplots()
    tempo = np.linspace(0, tempoEncontro, 1000)
    ypbola = -0.008*(tempo**2) + 0.4*tempo + 0.5
    yprobo = posRoboY + aceleRoboY*(tempo**2)/2
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
def graphPosX(posRoboX, posRoboY):
    if posRoboX < 0 or posRoboX > 9:
        msg()
        return
    elif posRoboY < 0 or posRoboY > 6:
        msg();
        return
    else:
        pass 
    raioRobo = 0.09 # metros
    raioIntercep = raioRobo + (1/3*raioRobo) + 0.0215
    aceleMax = 2 # m/s^s
    veloMax = 3 # m/s
    #posRoboX = float(input("Defina a posição inicial do robo em X no campo (m): "))
    #posRoboY = float(input("Defina a posição inicial do robo em Y no campo (m): "))

    # Dados da bola:
    v0B = 0.64 # m/s
    posBolaX = 1
    posBolaY = 0.5
    tempoTot = 0
    encontrou = False
    distRoboBola = sqrt(((posBolaX - posRoboX)**2) + ((posBolaY - posRoboY)**2))
    #print(distRoboBola)

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
    
    # if posRoboY >= -0.0309*(posRoboX**2) + 0.9215*posRoboX - 0.4366 and tan(direcao) > 0 or posRoboY < -0.0309*(posRoboX**2) + 0.9215*posRoboX - 0.4366 and tan(direcao) < 0:
    #     aceleRoboX = - abs(cos(direcao))*aceleRobo
    # elif posRoboY >= -0.0309*(posRoboX**2) + 0.9215*posRoboX - 0.4366 and tan(direcao) < 0 or posRoboY > -0.0309*(posRoboX**2) + 0.9215*posRoboX - 0.4366 and tan(direcao) > 0:
    #     aceleRoboX = abs(cos(direcao))*aceleRobo

    xpbola = -0.005*(tempoEncontro**2) + 0.5*tempoEncontro + 1
    if posRoboX > xpbola:
        aceleRoboX = - abs(cos(direcao))*aceleRobo
    else:
        aceleRoboX =   abs(cos(direcao))*aceleRobo


    fig, ax = plt.subplots()
    tempo = np.linspace(0, tempoEncontro, 1000)
    xpbola = -0.005*(tempo**2) + 0.5*tempo + 1
    xprobo = posRoboX + aceleRoboX*(tempo**2)/2
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
def graphVeloX(posRoboX, posRoboY):
    if posRoboX < 0 or posRoboX > 9:
        msg()
        return
    elif posRoboY < 0 or posRoboY > 6:
        msg();
        return
    else:
        pass 
    raioRobo = 0.09 # metros
    raioIntercep = raioRobo + (1/3*raioRobo) + 0.0215
    aceleMax = 2 # m/s^s
    veloMax = 3 # m/s
    #posRoboX = float(input("Defina a posição inicial do robo em X no campo (m): "))
    #posRoboY = float(input("Defina a posição inicial do robo em Y no campo (m): "))

    # Dados da bola:
    v0B = 0.64 # m/s
    posBolaX = 1
    posBolaY = 0.5
    tempoTot = 0
    encontrou = False
    distRoboBola = sqrt(((posBolaX - posRoboX)**2) + ((posBolaY - posRoboY)**2))
    #print(distRoboBola)

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
    # if posRoboY >= -0.0309*(posRoboX**2) + 0.9215*posRoboX - 0.4366 and tan(direcao) > 0 or posRoboY < -0.0309*(posRoboX**2) + 0.9215*posRoboX - 0.4366 and tan(direcao) < 0:
    #     aceleRoboX = - abs(cos(direcao))*aceleRobo
    # elif posRoboY >= -0.0309*(posRoboX**2) + 0.9215*posRoboX - 0.4366 and tan(direcao) < 0 or posRoboY > -0.0309*(posRoboX**2) + 0.9215*posRoboX - 0.4366 and tan(direcao) > 0:
    #     aceleRoboX = abs(cos(direcao))*aceleRobo

    xpbola = -0.005*(tempoEncontro**2) + 0.5*tempoEncontro + 1
    if posRoboX > xpbola:
        aceleRoboX = - abs(cos(direcao))*aceleRobo
    else:
        aceleRoboX =   abs(cos(direcao))*aceleRobo

    fig, ax = plt.subplots()
    tempo = np.linspace(0, tempoEncontro, 1000)
    xvbola = -0.010*tempo + 0.5
    xvrobo = aceleRoboX*(tempo)
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
def graphVeloY(posRoboX, posRoboY):
    if posRoboX < 0 or posRoboX > 9:
        msg()
        return
    elif posRoboY < 0 or posRoboY > 6:
        msg();
        return
    else:
        pass 
    raioRobo = 0.09 # metros
    raioIntercep = raioRobo + (1/3*raioRobo) + 0.0215
    aceleMax = 2 # m/s^s
    veloMax = 3 # m/s
    #posRoboX = float(input("Defina a posição inicial do robo em X no campo (m): "))
    #posRoboY = float(input("Defina a posição inicial do robo em Y no campo (m): "))

    # Dados da bola:
    v0B = 0.64 # m/s
    posBolaX = 1
    posBolaY = 0.5
    tempoTot = 0
    encontrou = False
    distRoboBola = sqrt(((posBolaX - posRoboX)**2) + ((posBolaY - posRoboY)**2))
    #print(distRoboBola)

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
    # if posRoboY >= -0.0309*(posRoboX**2) + 0.9215*posRoboX - 0.4366:
    #     aceleRoboY = - abs(sin(direcao))*aceleRobo
    # else:
    #     aceleRoboY = abs(sin(direcao))*aceleRobo

    ypbola = -0.008*(tempoEncontro**2) + 0.4*tempoEncontro + 0.5
    if posRoboY > ypbola:
        aceleRoboY = - abs(sin(direcao))*aceleRobo
    else:
        aceleRoboY = abs(sin(direcao))*aceleRobo


    fig, ax = plt.subplots()
    tempo = np.linspace(0, tempoEncontro, 1000)
    yvbola = -0.016*tempo + 0.4
    yvrobo = aceleRoboY*(tempo)
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
def graphAceleX(posRoboX, posRoboY):
    if posRoboX < 0 or posRoboX > 9:
        msg()
        return
    elif posRoboY < 0 or posRoboY > 6:
        msg();
        return
    else:
        pass 
    raioRobo = 0.09 # metros
    raioIntercep = raioRobo + (1/3*raioRobo) + 0.0215
    aceleMax = 2 # m/s^s
    veloMax = 3 # m/s
    #posRoboX = float(input("Defina a posição inicial do robo em X no campo (m): "))
    #posRoboY = float(input("Defina a posição inicial do robo em Y no campo (m): "))

    # Dados da bola:
    v0B = 0.64 # m/s
    posBolaX = 1
    posBolaY = 0.5
    tempoTot = 0
    encontrou = False
    distRoboBola = sqrt(((posBolaX - posRoboX)**2) + ((posBolaY - posRoboY)**2))
    #print(distRoboBola)

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
    # if posRoboY >= -0.0309*(posRoboX**2) + 0.9215*posRoboX - 0.4366 and tan(direcao) > 0 or posRoboY < -0.0309*(posRoboX**2) + 0.9215*posRoboX - 0.4366 and tan(direcao) < 0:
    #     aceleRoboX = - abs(cos(direcao))*aceleRobo
    # elif posRoboY >= -0.0309*(posRoboX**2) + 0.9215*posRoboX - 0.4366 and tan(direcao) < 0 or posRoboY > -0.0309*(posRoboX**2) + 0.9215*posRoboX - 0.4366 and tan(direcao) > 0:
    #     aceleRoboX = abs(cos(direcao))*aceleRobo

    xpbola = -0.005*(tempoEncontro**2) + 0.5*tempoEncontro + 1
    if posRoboX > xpbola:
        aceleRoboX = - abs(cos(direcao))*aceleRobo
    else:
        aceleRoboX =   abs(cos(direcao))*aceleRobo

    fig, ax = plt.subplots()
    tempo = np.linspace(0, tempoEncontro, 1000)
    xabola = -0.010*(tempo**0)
    xarobo = aceleRoboX*(tempo**0)
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
def graphAceleY(posRoboX, posRoboY):
    if posRoboX < 0 or posRoboX > 9:
        msg()
        return
    elif posRoboY < 0 or posRoboY > 6:
        msg();
        return
    else:
        pass 
    raioRobo = 0.09 # metros
    raioIntercep = raioRobo + (1/3*raioRobo) + 0.0215
    aceleMax = 2 # m/s^s
    veloMax = 3 # m/s
    #posRoboX = float(input("Defina a posição inicial do robo em X no campo (m): "))
    #posRoboY = float(input("Defina a posição inicial do robo em Y no campo (m): "))

    # Dados da bola:
    v0B = 0.64 # m/s
    posBolaX = 1
    posBolaY = 0.5
    tempoTot = 0
    encontrou = False
    distRoboBola = sqrt(((posBolaX - posRoboX)**2) + ((posBolaY - posRoboY)**2))
    #print(distRoboBola)

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
    # if posRoboY >= -0.0309*(posRoboX**2) + 0.9215*posRoboX - 0.4366:
    #     aceleRoboY = - abs(sin(direcao))*aceleRobo
    # else:
    #     aceleRoboY = abs(sin(direcao))*aceleRobo

    ypbola = -0.008*(tempoEncontro**2) + 0.4*tempoEncontro + 0.5
    if posRoboY > ypbola:
        aceleRoboY = - abs(sin(direcao))*aceleRobo
    else:
        aceleRoboY = abs(sin(direcao))*aceleRobo


    fig, ax = plt.subplots()
    tempo = np.linspace(0, tempoEncontro, 1000)
    yabola = -0.016*(tempo**0)
    yarobo = aceleRoboY*(tempo**0)
    plt.plot(tempo, yabola, label = 'Bola')
    plt.plot(tempo, yarobo, label = 'Robo')

    #Personalizações do Gráfico
    plt.xlabel("Tempo (s)")
    plt.ylabel("Aceleração Y (m/s^2)")
    plt.title("Aceleração Y / Tempo")
    plt.grid()
    plt.legend()

    # Printar o gráfico
    plt.show()

def graphDistRel(posRoboX, posRoboY):
    if posRoboX < 0 or posRoboX > 9:
        msg()
        return
    elif posRoboY < 0 or posRoboY > 6:
        msg();
        return
    else:
        pass 
    raioRobo = 0.09 # metros
    raioIntercep = raioRobo + (1/3*raioRobo) + 0.0215
    aceleMax = 2 # m/s^s
    veloMax = 3 # m/s
    #posRoboX = float(input("Defina a posição inicial do robo em X no campo (m): "))
    #posRoboY = float(input("Defina a posição inicial do robo em Y no campo (m): "))

    # Dados da bola:
    v0B = 0.64 # m/s
    posBolaX = 1
    posBolaY = 0.5
    tempoTot = 0
    encontrou = False
    distRoboBola = sqrt(((posBolaX - posRoboX)**2) + ((posBolaY - posRoboY)**2))
    #print(distRoboBola)

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

    
    # if posRoboY >= -0.0309*(posRoboX**2) + 0.9215*posRoboX - 0.4366:
    #     aceleRoboY = - abs(sin(direcao))*aceleRobo
    # else:
    #     aceleRoboY = abs(sin(direcao))*aceleRobo

    ypbola = -0.008*(tempoEncontro**2) + 0.4*tempoEncontro + 0.5
    if posRoboY > ypbola:
        aceleRoboY = - abs(sin(direcao))*aceleRobo
    else:
        aceleRoboY = abs(sin(direcao))*aceleRobo


    # if posRoboY >= -0.0309*(posRoboX**2) + 0.9215*posRoboX - 0.4366 and tan(direcao) > 0 or posRoboY < -0.0309*(posRoboX**2) + 0.9215*posRoboX - 0.4366 and tan(direcao) < 0:
    #     aceleRoboX = - abs(cos(direcao))*aceleRobo
    # elif posRoboY >= -0.0309*(posRoboX**2) + 0.9215*posRoboX - 0.4366 and tan(direcao) < 0 or posRoboY > -0.0309*(posRoboX**2) + 0.9215*posRoboX - 0.4366 and tan(direcao) > 0:
    #     aceleRoboX = abs(cos(direcao))*aceleRobo


    xpbola = -0.005*(tempoEncontro**2) + 0.5*tempoEncontro + 1
    if posRoboX > xpbola:
        aceleRoboX = - abs(cos(direcao))*aceleRobo
    else:
        aceleRoboX =   abs(cos(direcao))*aceleRobo



    fig, ax = plt.subplots()
    tempo = np.linspace(0, tempoEncontro, 1000)

    # yprobo = posRoboY + aceleRoboY*(tempo**2)/2
    # ypbola = -0.008*(tempo**2) + 0.4*tempo + 0.5
    # xprobo = posRoboX + aceleRoboX*(tempo**2)/2
    # xpbola = -0.005*(tempo**2) + 0.5*tempo + 1

    distRel = np.sqrt(((-0.008*(tempo**2) + 0.4*tempo + 0.5) - (posRoboY + aceleRoboY*(tempo**2)/2))**2 + ((-0.005*(tempo**2) + 0.5*tempo + 1) - (posRoboX + aceleRoboX*(tempo**2)/2))**2)
    plt.plot(tempo, distRel, label = 'Distância Relativa Robo-Bola')

    #Personalizações do Gráfico
    plt.xlabel("Tempo (s)")
    plt.ylabel("Distância Relativa (m)")
    plt.title("Distância Relativa / Tempo")
    plt.grid()
    plt.legend()

    # Printar o gráfico
    plt.show()

def graphEnergiaCinet(posRoboX, posRoboY):
    if posRoboX < 0 or posRoboX > 9:
        msg()
        return
    elif posRoboY < 0 or posRoboY > 6:
        msg();
        return
    else:
        pass 
    raioRobo = 0.09 # metros
    raioIntercep = raioRobo + (1/3*raioRobo) + 0.0215
    aceleMax = 2 # m/s^s
    veloMax = 3 # m/s
    #posRoboX = float(input("Defina a posição inicial do robo em X no campo (m): "))
    #posRoboY = float(input("Defina a posição inicial do robo em Y no campo (m): "))

    # Dados da bola:
    v0B = 0.64 # m/s
    posBolaX = 1
    posBolaY = 0.5
    tempoTot = 0
    encontrou = False
    distRoboBola = sqrt(((posBolaX - posRoboX)**2) + ((posBolaY - posRoboY)**2))
    #print(distRoboBola)

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

    aceleBola = 0.019 # (m/s^2)
    mRobo = 2.8 # (Kg)
    mBola = 0.045 # (Kg)

    fig, ax = plt.subplots()
    tempo = np.linspace(0, tempoEncontro, 1000)
    veloRob = aceleRobo*tempo
    veloBola = aceleBola*tempo
    ecBola = mBola*(veloBola**2)/2
    ecRobo = mRobo*(veloRob**2)/2 
    plt.plot(tempo, ecBola, label = 'Bola')
    plt.plot(tempo, ecRobo, label = 'Robo')

    #Personalizações do Gráfico
    plt.xlabel("Tempo (s)")
    plt.ylabel("Energia Cinética (J)")
    plt.title("Energia Cinética / Tempo")
    plt.grid()
    plt.legend()

    # Printar o gráfico
    plt.show()


posY = Button(janela, text="Posição Y por Tempo", font=("Times New Roman", 15), command= lambda: graphPosY(float(posRoboX.get()), float(posRoboY.get())))
posY.place(relx=0.7, rely=0.32, anchor=CENTER)

posX = Button(janela, text="Posição X por Tempo", font=("Times New Roman", 15), command= lambda: graphPosX(float(posRoboX.get()), float(posRoboY.get())))
posX.place(relx=0.3, rely=0.32, anchor=CENTER)

veloX = Button(janela, text="Velocidade em X por Tempo", font=("Times New Roman", 15), command= lambda: graphVeloX(float(posRoboX.get()), float(posRoboY.get())))
veloX.place(relx=0.3, rely=0.52, anchor=CENTER)

veloY = Button(janela, text="Velocidade em Y por Tempo", font=("Times New Roman", 15), command= lambda: graphVeloY(float(posRoboX.get()), float(posRoboY.get())))
veloY.place(relx=0.7, rely=0.52, anchor=CENTER)

aceX= Button(janela, text="Aceleração em X por Tempo", font=("Times New Roman", 15), command= lambda: graphAceleX(float(posRoboX.get()), float(posRoboY.get())))
aceX.place(relx=0.3, rely=0.72, anchor=CENTER)

aceY= Button(janela, text="Aceleração em Y por Tempo", font=("Times New Roman", 15), command= lambda: graphAceleY(float(posRoboX.get()), float(posRoboY.get())))
aceY.place(relx=0.7, rely=0.72, anchor=CENTER)

distRela= Button(janela, text="Distância Relativa por Tempo", font=("Times New Roman", 15), command= lambda: graphDistRel(float(posRoboX.get()), float(posRoboY.get())))
distRela.place(relx=0.3, rely=0.92, anchor=CENTER)

trajeto = Button(janela, text="Trajetoria no Campo", font=("Times New Roman", 15), command= lambda: graphTrajetoCampo(float(posRoboX.get()), float(posRoboY.get())))
trajeto.place(relx=0.7, rely=0.92, anchor=CENTER)

ecinet = Button(janela, text="Energia Cinética", font=("Times New Roman", 15), command= lambda: graphEnergiaCinet(float(posRoboX.get()), float(posRoboY.get())))
ecinet.place(relx=0.89, rely=0.1, anchor=CENTER)


janela.mainloop()