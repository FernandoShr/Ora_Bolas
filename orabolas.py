import matplotlib.pyplot as plt
import numpy as np
from math import *
from tkinter import *
from tkinter import messagebox

######### Dados internos do robo e da bola #########

### Robo ###
# modelo: small size
# raioRobo = 0.09 # metros
# aceleMax = 2 # m/s^s
# veloMax = 3 # m/s

### Bola ###
# velocidade inicial = 0.64 # m/s
# posição incial da bola em X = 1
# posição incial da bola em Y = 0.5

# Janela Tkinter
janela = Tk()
janela.geometry("700x350")
janela.title("Ora Bolas")
janela.configure(bg='#9FFFF6')

# Campos de entrada para as posições iniciais do Robô:
t1 = Label(janela, text="Posição inicial do Robô em X:", font=("Times New Roman",13), bg='#9FFFF6')
t1.place(relx=0.48, rely=0.02, anchor=NE)
posRoboX = Entry(janela, width=20, font=("Times New Roman", 13))
posRoboX.place(relx=0.5, rely=0.02, anchor=NW)

t2 = Label(janela, text="Posição inicial do Robô em Y:", font=("Times New Roman",13), bg='#9FFFF6')
t2.place(relx=0.48, rely=0.1, anchor=NE)
posRoboY = Entry(janela, width=20, font=("Times New Roman", 13))
posRoboY.place(relx=0.5, rely=0.1, anchor=NW)


# Função para alertar o usuário caso insira algum valor inválido
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

    # Dados do robo:
    aceleMax = 2 # m/s^s
    veloMax = 3 # m/s

    # Dados da bola:
    posBolaX = 1
    posBolaY = 0.5
    tempoTot = 0

    # Encontrar a bola:
    while tempoTot <= 20:
        yB = -0.008*(tempoTot**2) + 0.4*tempoTot + 0.5
        xB = -0.005*(tempoTot**2) + 0.5*tempoTot + 1

        posBolaY = yB
        posBolaX = xB
        distRoboBola = sqrt(((posBolaX - posRoboX)**2) + ((posBolaY - posRoboY)**2))

        if tempoTot != 0:
            acelePrecisa = (2*distRoboBola)/(tempoTot**2)
            
            veloPrecisa = acelePrecisa*tempoTot
            if acelePrecisa > aceleMax or veloPrecisa > veloMax:
                pass
            else:
                direcao = atan((posBolaY - posRoboY)/(posBolaX - posRoboX))
                tempoEncontro = tempoTot
                break

        tempoTot += 0.02

    # Monta o Gráfico
    fig, ax = plt.subplots()
    xpbola = -0.005*(tempoEncontro**2) + 0.5*tempoEncontro + 1
    x = np.linspace(1, 9, 1000)
    xpB = np.linspace(1, xpbola, 1000)
    ybola = -0.0309*(x**2) + 0.9215*x - 0.4366
    ybolalim = -0.0309*(xpB**2) + 0.9215*xpB - 0.4366
    xpLimitebola = -0.005*(tempoEncontro**2) + 0.5*tempoEncontro + 1
    rx = np.linspace(posRoboX, xpLimitebola, 1000)
    yrobo = tan(direcao)*(rx - posRoboX) + posRoboY
    ax.plot(xpB,ybolalim, label='Bola',color='blue')
    ax.plot(rx,yrobo, label='Robo', color='orange')
    ax.plot(x,ybola, label = 'Trajeto da bola (sem interceptação)' ,ls='--', color='blue')

    # Personalizações do Gráfico
    plt.xlabel("Posição X (m)")
    plt.ylabel("Posição Y (m)")
    plt.title("Trajetoria Campo")
    plt.legend()

    # Mostra o Gráfico
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

    # Dados do Robo:
    aceleMax = 2 # m/s^s
    veloMax = 3 # m/s

    # Dados da bola:
    posBolaX = 1
    posBolaY = 0.5
    tempoTot = 0

    # Encontrar a bola:
    while tempoTot <= 20:
        yB = -0.008*(tempoTot**2) + 0.4*tempoTot + 0.5
        xB = -0.005*(tempoTot**2) + 0.5*tempoTot + 1

        posBolaY = yB
        posBolaX = xB
        distRoboBola = sqrt(((posBolaX - posRoboX)**2) + ((posBolaY - posRoboY)**2))

        if tempoTot != 0:
            acelePrecisa = (2*distRoboBola)/(tempoTot**2)
            
            veloPrecisa = acelePrecisa*tempoTot
            if acelePrecisa > aceleMax or veloPrecisa > veloMax:
                pass
            else:
                aceleRobo = acelePrecisa
                direcao = atan((posBolaY - posRoboY)/(posBolaX - posRoboX))
                tempoEncontro = tempoTot
                break

        tempoTot += 0.02

    # Determina a direção da aceleração do robo
    ypbola = -0.008*(tempoEncontro**2) + 0.4*tempoEncontro + 0.5
    if posRoboY > ypbola:
        aceleRoboY = - abs(sin(direcao))*aceleRobo
    else:
        aceleRoboY = abs(sin(direcao))*aceleRobo

    # Monta o Gráfico
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

    # Dados do Robo:
    aceleMax = 2 # m/s^s
    veloMax = 3 # m/s

    # Dados da bola:
    v0B = 0.64 # m/s
    posBolaX = 1
    posBolaY = 0.5
    tempoTot = 0


    # Encontrar a bola:
    while tempoTot <= 20:
        yB = -0.008*(tempoTot**2) + 0.4*tempoTot + 0.5
        xB = -0.005*(tempoTot**2) + 0.5*tempoTot + 1

        posBolaY = yB
        posBolaX = xB
        distRoboBola = sqrt(((posBolaX - posRoboX)**2) + ((posBolaY - posRoboY)**2))

        if tempoTot != 0:
            acelePrecisa = (2*distRoboBola)/(tempoTot**2)
            
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
    
    # Determina a direção da aceleração do robo
    xpbola = -0.005*(tempoEncontro**2) + 0.5*tempoEncontro + 1
    if posRoboX > xpbola:
        aceleRoboX = - abs(cos(direcao))*aceleRobo
    else:
        aceleRoboX =   abs(cos(direcao))*aceleRobo

    # Monta o Gráfico
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
    
    # Dados do Robo:
    aceleMax = 2 # m/s^s
    veloMax = 3 # m/s


    # Dados da bola:
    posBolaX = 1
    posBolaY = 0.5
    tempoTot = 0
  

    # Encontrar a bola:
    while tempoTot <= 20:
        yB = -0.008*(tempoTot**2) + 0.4*tempoTot + 0.5
        xB = -0.005*(tempoTot**2) + 0.5*tempoTot + 1

        posBolaY = yB
        posBolaX = xB
        distRoboBola = sqrt(((posBolaX - posRoboX)**2) + ((posBolaY - posRoboY)**2))

        if tempoTot != 0:
            acelePrecisa = (2*distRoboBola)/(tempoTot**2)
            
            veloPrecisa = acelePrecisa*tempoTot
            if acelePrecisa > aceleMax or veloPrecisa > veloMax:
                pass
            else:
                aceleRobo = acelePrecisa
                direcao = atan((posBolaY - posRoboY)/(posBolaX - posRoboX))
                tempoEncontro = tempoTot
                break

        tempoTot += 0.02

    # Determina a direção da aceleração do robo
    xpbola = -0.005*(tempoEncontro**2) + 0.5*tempoEncontro + 1
    if posRoboX > xpbola:
        aceleRoboX = - abs(cos(direcao))*aceleRobo
    else:
        aceleRoboX =   abs(cos(direcao))*aceleRobo

    # Monta o Gráfico
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

    # Dados do Robo:
    aceleMax = 2 # m/s^s
    veloMax = 3 # m/s


    # Dados da bola:
    posBolaX = 1
    posBolaY = 0.5
    tempoTot = 0
    distRoboBola = sqrt(((posBolaX - posRoboX)**2) + ((posBolaY - posRoboY)**2))
  

    # Encontrar a bola:
    while tempoTot <= 20:
        yB = -0.008*(tempoTot**2) + 0.4*tempoTot + 0.5
        xB = -0.005*(tempoTot**2) + 0.5*tempoTot + 1

        posBolaY = yB
        posBolaX = xB
        distRoboBola = sqrt(((posBolaX - posRoboX)**2) + ((posBolaY - posRoboY)**2))

        if tempoTot != 0:
            acelePrecisa = (2*distRoboBola)/(tempoTot**2)
            
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

    # Determina a direção da aceleração do robo
    ypbola = -0.008*(tempoEncontro**2) + 0.4*tempoEncontro + 0.5
    if posRoboY > ypbola:
        aceleRoboY = - abs(sin(direcao))*aceleRobo
    else:
        aceleRoboY = abs(sin(direcao))*aceleRobo

    # Monta o Gráfico
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

    # Dados Robo:
    aceleMax = 2 # m/s^s
    veloMax = 3 # m/s
  

    # Dados da bola:
    posBolaX = 1
    posBolaY = 0.5
    tempoTot = 0


    # Encontrar a bola:
    while tempoTot <= 20:
        yB = -0.008*(tempoTot**2) + 0.4*tempoTot + 0.5
        xB = -0.005*(tempoTot**2) + 0.5*tempoTot + 1

        posBolaY = yB
        posBolaX = xB
        distRoboBola = sqrt(((posBolaX - posRoboX)**2) + ((posBolaY - posRoboY)**2))

        if tempoTot != 0:
            acelePrecisa = (2*distRoboBola)/(tempoTot**2)
            
            veloPrecisa = acelePrecisa*tempoTot
            if acelePrecisa > aceleMax or veloPrecisa > veloMax:
                pass
            else:
                aceleRobo = acelePrecisa
                direcao = atan((posBolaY - posRoboY)/(posBolaX - posRoboX))
                tempoEncontro = tempoTot
                break

        tempoTot += 0.02
  
    # Determina a direção da aceleração do robo
    xpbola = -0.005*(tempoEncontro**2) + 0.5*tempoEncontro + 1
    if posRoboX > xpbola:
        aceleRoboX = - abs(cos(direcao))*aceleRobo
    else:
        aceleRoboX =   abs(cos(direcao))*aceleRobo

    # Monta o Gráfico
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

    # Dados do Robo
    aceleMax = 2 # m/s^s
    veloMax = 3 # m/s

    # Dados da bola:
    posBolaX = 1
    posBolaY = 0.5
    tempoTot = 0

    # Encontrar a bola:
    while tempoTot <= 20:
        yB = -0.008*(tempoTot**2) + 0.4*tempoTot + 0.5
        xB = -0.005*(tempoTot**2) + 0.5*tempoTot + 1

        posBolaY = yB
        posBolaX = xB
        distRoboBola = sqrt(((posBolaX - posRoboX)**2) + ((posBolaY - posRoboY)**2))

        if tempoTot != 0:
            acelePrecisa = (2*distRoboBola)/(tempoTot**2)
            
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

    # Determina a aceleração em Y
    ypbola = -0.008*(tempoEncontro**2) + 0.4*tempoEncontro + 0.5
    if posRoboY > ypbola:
        aceleRoboY = - abs(sin(direcao))*aceleRobo
    else:
        aceleRoboY = abs(sin(direcao))*aceleRobo


    # Monta o Gráfico
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

###### Gráficos Distancia Relativa/Tempo ##########
def graphDistRel(posRoboX, posRoboY):
    if posRoboX < 0 or posRoboX > 9:
        msg()
        return
    elif posRoboY < 0 or posRoboY > 6:
        msg();
        return
    else:
        pass 

    # Dados do Robô
    aceleMax = 2 # m/s^s
    veloMax = 3 # m/s


    # Dados da bola:
    posBolaX = 1
    posBolaY = 0.5
    tempoTot = 0


    # Encontrar a bola:
    while tempoTot <= 20:
        yB = -0.008*(tempoTot**2) + 0.4*tempoTot + 0.5
        xB = -0.005*(tempoTot**2) + 0.5*tempoTot + 1

        posBolaY = yB
        posBolaX = xB
        distRoboBola = sqrt(((posBolaX - posRoboX)**2) + ((posBolaY - posRoboY)**2))

        if tempoTot != 0:
            acelePrecisa = (2*distRoboBola)/(tempoTot**2)
            
            veloPrecisa = acelePrecisa*tempoTot
            if acelePrecisa > aceleMax or veloPrecisa > veloMax:
                pass
            else:
                aceleRobo = acelePrecisa
                direcao = atan((posBolaY - posRoboY)/(posBolaX - posRoboX))
                tempoEncontro = tempoTot
                break

        tempoTot += 0.02

    
    # Define as acelerações do Robô nas direções X e Y:

    ypbola = -0.008*(tempoEncontro**2) + 0.4*tempoEncontro + 0.5
    if posRoboY > ypbola:
        aceleRoboY = - abs(sin(direcao))*aceleRobo
    else:
        aceleRoboY = abs(sin(direcao))*aceleRobo



    xpbola = -0.005*(tempoEncontro**2) + 0.5*tempoEncontro + 1
    if posRoboX > xpbola:
        aceleRoboX = - abs(cos(direcao))*aceleRobo
    else:
        aceleRoboX =   abs(cos(direcao))*aceleRobo


    # Monta o Gráfico
    tempo = np.linspace(0, tempoEncontro, 1000)
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


###### Energia Cinética/Tempo ##########
def graphEnergiaCinet(posRoboX, posRoboY):
    if posRoboX < 0 or posRoboX > 9:
        msg()
        return
    elif posRoboY < 0 or posRoboY > 6:
        msg();
        return
    else:
        pass 

    # Dados do robo:
    aceleMax = 2 # m/s^s
    veloMax = 3 # m/s


    # Dados da bola:
    posBolaX = 1
    posBolaY = 0.5
    tempoTot = 0


    # Encontrar a bola:
    while tempoTot <= 20:
        yB = -0.008*(tempoTot**2) + 0.4*tempoTot + 0.5
        xB = -0.005*(tempoTot**2) + 0.5*tempoTot + 1

        posBolaY = yB
        posBolaX = xB
        distRoboBola = sqrt(((posBolaX - posRoboX)**2) + ((posBolaY - posRoboY)**2))

        if tempoTot != 0:
            acelePrecisa = (2*distRoboBola)/(tempoTot**2)
            
            veloPrecisa = acelePrecisa*tempoTot
            if acelePrecisa > aceleMax or veloPrecisa > veloMax:
                pass
            else:
                aceleRobo = acelePrecisa
                tempoEncontro = tempoTot
                break
        tempoTot += 0.02

    aceleBola = 0.019 # (m/s^2)
    mRobo = 2.8 # (Kg)
    mBola = 0.045 # (Kg)

    # Monta o Gráfico
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


# Botões de interação na interface:

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

# Manter o Tkinter aberto
janela.mainloop()