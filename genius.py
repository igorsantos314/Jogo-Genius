from tkinter import *
from time import sleep
import _thread as th
from random import randint
from tkinter import messagebox

janela = Tk()
janela.geometry('800x800')
janela['background'] = 'black'


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

def movimento():
    #modifica a cor spera 1seg --> e zera novamente
    for i in range(nivel):
        sleep(1)
        
        numeroAleatorio = randint(1,4)
        print(numeroAleatorio)
        mudarCor(numeroAleatorio)
        addCores(numeroAleatorio)

        sleep(1)
        zerarCores()

    #volta as cores default
    setColorOrigin()
    messagebox.showinfo('GENIUS','É A SUA VEZ!')

    #retira o botão de inicio de jogo
    btInicioJogo.destroy()

    #limpa a lista de cores dos jogadores
    listaCoresPlayer.clear()
    print(listaCores)

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
    print(listaCoresPlayer)

    #quantidade de elementos de cada lista sejam iguais, e diferentes de 0
    if len(listaCores) == len(listaCoresPlayer) and len(listaCores) != 0:

        #caso as listas sejam iguais o usuario acertou o padrao
        if listaCores == listaCoresPlayer:
            #eleva o nivel e recomeça a sequencia
            messagebox.showinfo('','V O C Ê  A C E R T O U  !')
            nivel += 1

            #limpa a lista anterior
            listaCores.clear()

            #continua jogando almentando o nivel
            start()

        else:
            #reconstroi a tela e zera o nivel
            messagebox.showinfo('','V O C Ê  P E R D E U !')
            nivel = 1

            #apaga e reconstroi a tela
            reconstruct()

    if len(listaCoresPlayer) != 0:
        #atualiza o nivel para o usuário
        lblNivel['text'] = str(nivel)

def construct():

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

    btBlue = Button(text='', width='15', height='10', bg='cyan', command= lambda: addCoresRespota(1))
    btBlue.place(x=250,y=50)

    btGreen = Button(text='', width='15', height='10', bg='green', command= lambda: addCoresRespota(2))
    btGreen.place(x=420,y=50)

    btRed = Button(text='', width='15', height='10', bg='red', command= lambda: addCoresRespota(3))
    btRed.place(x=250,y=240)

    btYellow = Button(text='', width='15', height='10', bg='yellow', command= lambda: addCoresRespota(4))
    btYellow.place(x=420,y=240)

    btInicioJogo = Button(text='Start', width='20', height='2', font='Courier 20 bold', bg='orange', command=start)
    btInicioJogo.place(x=240, y=450)

    lblNomeNivel = Label(text='', font='Courier 20 bold', fg='white', bg='black')
    lblNomeNivel.place(x=20,y=20)

    lblNivel = Label(text='', font='Courier 20 bold', fg='orange', bg='black')
    lblNivel.place(x=140,y=20)

#th.start_new_thread(movimento, (250,))
construct()
janela.mainloop()