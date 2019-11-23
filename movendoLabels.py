from tkinter import *
from time import sleep
import _thread as th
from random import randint
from tkinter import messagebox

janela = Tk()
janela.geometry('1000x800')
janela['background'] = 'black'


def start():
    zerarCores()
    th.start_new_thread(movimento, (5,))

def zerarCores():
    btBlue['bg'] = 'white'
    btGreen['bg'] = 'white'
    btRed['bg'] = 'white'
    btYellow['bg'] = 'white'

def setColorOrigin():
    for i in range(1,5):
        mudarCor(i)

def mudarCor(indBotao):
    if indBotao == 1:
        btBlue['bg'] = 'cyan'
    
    elif indBotao == 2:
        btGreen['bg'] = 'green'

    elif indBotao == 3:
        btRed['bg'] = 'red'

    elif indBotao == 4:
        btYellow['bg'] = 'yellow'

def movimento(pos):
    for i in range(pos):
        sleep(1)
        
        numeroAleatorio = randint(1,4)
        print(numeroAleatorio)
        mudarCor(numeroAleatorio)
        addCores(numeroAleatorio)

        sleep(1)
        zerarCores()

    setColorOrigin()
    messagebox.showinfo('GENIUS','É A SUA VEZ!')
    btInicioJogo.destroy()

    listaCoresPlayer.clear()
    print(listaCores)

def reconstruct():
    btBlue.destroy()
    btGreen.destroy()
    btRed.destroy()
    btYellow.destroy()
    btInicioJogo.destroy()

    construct()

def addCores(valor):
    listaCores.append(valor)

def addCoresRespota(valor):
    listaCoresPlayer.append(valor)
    print(listaCoresPlayer)

    if len(listaCores) == len(listaCoresPlayer) and len(listaCores) != 0:
        if listaCores == listaCoresPlayer:
            messagebox.showinfo('','V O C Ê  A C E R T O U  !')

        else:
            messagebox.showinfo('','V O C Ê  P E R D E U !')

        reconstruct()

def construct():

    global btBlue
    global btGreen
    global btRed
    global btYellow
    global btInicioJogo

    global listaCores
    global listaCoresPlayer

    listaCores = []
    listaCoresPlayer = []

    btBlue = Button(text='', width='15', height='10', bg='cyan', command= lambda: addCoresRespota(1))
    btBlue.place(x=350,y=250)

    btGreen = Button(text='', width='15', height='10', bg='green', command= lambda: addCoresRespota(2))
    btGreen.place(x=520,y=250)

    btRed = Button(text='', width='15', height='10', bg='red', command= lambda: addCoresRespota(3))
    btRed.place(x=350,y=440)

    btYellow = Button(text='', width='15', height='10', bg='yellow', command= lambda: addCoresRespota(4))
    btYellow.place(x=520,y=440)

    btInicioJogo = Button(text='Start', width='20', height='2', font='Courier 20 bold', command=start)
    btInicioJogo.place(x=340, y=650)

#th.start_new_thread(movimento, (250,))
construct()
janela.mainloop()