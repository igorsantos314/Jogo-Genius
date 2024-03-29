from tkinter import *
from time import sleep
import _thread as th
from random import randint
from tkinter import messagebox

janela = Tk()
janela.geometry('1000x1000')
janela['background'] = 'black'

#listaCores
Colors = []

def start():
    #aparecer o nivel para o usuário
    lblNomeNivel['text'] = 'Nivel: '
    lblNivel['text'] = '1'

    #inicia um novo thread e deixa todos branco
    zerarCores()
    th.start_new_thread(movimento, ())

def zerarCores():
    #todos os botoes ficam branco
    btBlue['bg'] = 'white'
    btGreen['bg'] = 'white'
    btRed['bg'] = 'white'
    btYellow['bg'] = 'white'

def setColorOrigin():
    #mudar todas as cores para dafault
    for i in range(1,5):
        mudarCor(i)

def mudarCor(indBotao):
    #mudar a cor do botão com base na cor
    if indBotao == 1:
        btBlue['bg'] = 'cyan'
    
    elif indBotao == 2:
        btGreen['bg'] = 'green'

    elif indBotao == 3:
        btRed['bg'] = 'red'

    elif indBotao == 4:
        btYellow['bg'] = 'yellow'

def addCorSequencia(n):
    Colors.append(n)

def movimento():
    #modifica a cor spera 1seg --> e zera novamente
    numeroAleatorio = randint(1,4)
    addCorSequencia(numeroAleatorio)

    for i in Colors:
        sleep(0.8)
        #print(numeroAleatorio)
        mudarCor(i)
        #addCores(numeroAleatorio)
        sleep(0.8)
        zerarCores()

    #volta as cores default
    setColorOrigin()
    messagebox.showinfo('GENIUS','É  A  S U A  V E Z !')

    #retira o botão de inicio de jogo
    btInicioJogo.destroy()

    #limpa a lista de cores dos jogadores
    listaCoresPlayer.clear()
    #print(listaCores)

def reconstruct():
    #ocultar Nivel
    lblNomeNivel.destroy()
    lblNivel.destroy()

    #apaga tudo e reconstroi
    btBlue.destroy()
    btGreen.destroy()
    btRed.destroy()
    btYellow.destroy()
    btInicioJogo.destroy()

    #reconstroi a tela
    construct()

def addCores(valor):
    #adicionar as cores sorteadas
    listaCores.append(valor)

def addCoresRespota(valor):
    global nivel

    #adiciona o valor da respota do usuario na lista
    listaCoresPlayer.append(valor)
    #print(listaCoresPlayer)

    #quantidade de elementos de cada lista sejam iguais, e diferentes de 0
    if len(Colors) == len(listaCoresPlayer) and len(Colors) != 0:

        #caso as listas sejam iguais o usuario acertou o padrao
        if Colors == listaCoresPlayer:
            #eleva o nivel e recomeça a sequencia
            messagebox.showinfo('','V O C Ê  A C E R T O U  !')
            nivel += 1

            #limpa a lista anterior
            #listaCores.clear()

            #continua jogando almentando o nivel
            start()

        else:
            #reconstroi a tela e zera o nivel
            messagebox.showinfo('','V O C Ê  P E R D E U !')
            Colors.clear()
            #th.start_new_thread(louse,())
            nivel = 1

            #apaga e reconstroi a tela
            reconstruct()

    if len(listaCoresPlayer) != 0:
        #atualiza o nivel para o usuário
        lblNivel['text'] = str(nivel)

"""def louse():
    perder = Tk()
    #perder.geometry('100x100')
    perder.title(' N Ã O  F O I  D E S S A  V E Z  :(')

    lblPerdeu = Label(perder, text=' T E N T E  N O V A M E N T E  ...')
    lblPerdeu.pack()

    sleep(3)
    perder.destroy()
    
    perder.mainloop()"""

def construct():
    #tJogo.destroy()
    #janela principal

    #Labels globais
    global lblNomeNivel
    global lblNivel

    #botoes globais
    global btBlue
    global btGreen
    global btRed
    global btYellow
    global btInicioJogo

    #listas globais
    global listaCores
    global listaCoresPlayer

    #variaveis globais
    global nivel
    nivel = 1

    listaCores = []
    listaCoresPlayer = []

    """
    Config para Tela grande:
    btBlue.place(x=350,y=250)
    btGreen.place(x=520,y=250)
    btRed.place(x=350,y=440)
    btYellow.place(x=520,y=440)
    btInicioJogo.place(x=340, y=650)
    """

    btBlue = Button(text='', width='20', height='10', bg='cyan', command= lambda: addCoresRespota(1))
    btBlue.place(x=350,y=250)

    btGreen = Button(text='', width='20', height='10', bg='green', command= lambda: addCoresRespota(2))
    btGreen.place(x=520,y=250)

    btRed = Button(text='', width='20', height='10', bg='red', command= lambda: addCoresRespota(3))
    btRed.place(x=350,y=440)

    btYellow = Button(text='', width='20', height='10', bg='yellow', command= lambda: addCoresRespota(4))
    btYellow.place(x=520,y=440)

    btInicioJogo = Button(text='Start', width='22', height='2', font='Courier 20 bold', bg='orange', command=start)
    btInicioJogo.place(x=330, y=650)

    lblNomeNivel = Label(text='', font='Courier 20 bold', fg='white', bg='black')
    lblNomeNivel.place(x=20,y=20)

    lblNivel = Label(text='', font='Courier 20 bold', fg='orange', bg='black')
    lblNivel.place(x=140,y=20)

    
#th.start_new_thread(movimento, (250,))
construct()
janela.mainloop()
