import cv2 as cv #Precisa baixar
import tkinter as tk #Precisa baixar
from tkinter import *
from PIL import Image, ImageTk #Precisa baixar
import os

#Função tela sobre
def telaSobre():
    tela_principal.withdraw()
    tela_sobre = tk.Toplevel(tela_principal)
    screen_width = tela_sobre.winfo_screenwidth()
    screen_width = (screen_width/2) - (500/2)
    screen_height = tela_sobre.winfo_screenheight()
    screen_height = (screen_height/2) - (500/2)  
    tela_sobre.geometry('500x500+%d+%d' % (screen_width, screen_height)) #Tamanho
    tela_sobre.title('Sobre')

    tela_principal.wait_window(tela_sobre)
    if(tk.Toplevel.winfo_exists(tela_sobre) == 0):
        tela_principal.deiconify()

#Função tela registro
def telaRegistro():
    tela_principal.withdraw()
    tela_registro = tk.Toplevel(tela_principal)
    screen_width = tela_registro.winfo_screenwidth()
    screen_width = (screen_width/2) - (1000/2)
    screen_height = tela_registro.winfo_screenheight()
    screen_height = (screen_height/2) - (500/2)  
    tela_registro.geometry('1000x500+%d+%d' % (screen_width, screen_height)) #Tamanho
    tela_registro.title('Registro')
    webcam = tk.Label(tela_registro)
    webcam.place(x=15, y=10)
    cod = tk.Entry(tela_registro)
    cod.place(x=750, y=200)
    registrarButton = tk.Button(tela_registro, text="Registrar", command=lambda: registrar(cod, camera) ,height=1, width=20, border=10)
    registrarButton.place(x=750, y=400)

    #Acessar a camera
    camera = cv.VideoCapture(0)
    pegarFrames(camera,webcam)#Capturar os frames com a webcam

    tela_principal.wait_window(tela_registro)
    if(tk.Toplevel.winfo_exists(tela_registro) == 0):
        tela_principal.deiconify()

#Função para pegar frames e colocar em um painel tk
def pegarFrames(camera, webcam):
    ret, frame = camera.read()
    imagem = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    imagemPil = Image.fromarray(imagem) #Converter o ultimo frame recebido para pillow
    imagemTk = ImageTk.PhotoImage(image=imagemPil) #Converter o ultimo frame recebido em pillow para Tk 
    webcam.imagemTk = imagemTk
    webcam.configure(image=imagemTk)
    webcam.after(28, lambda: pegarFrames(camera,webcam))

#Função registrar
def registrar(cod,camera):
    cod = cod.get() #Aqui to recebendo o que tem no campo cod
    ret, face = camera.read() #Aqui to pegando 1 frame no momento em que o cara clicar no register
    
    if(os.path.exists('C:/EPI_CONTROL/FACES') == False):
        os.makedirs('C:/EPI_CONTROL/FACES')

    if(os.path.exists('C:/EPI_CONTROL/REGISTRO') == False):
        os.makedirs('C:/EPI_CONTROL/REGISTRO')

    if(os.path.exists('C:/EPI_CONTROL/MOVIMENTACAO') == False):
        os.makedirs('C:/EPI_CONTROL/MOVIMENTACAO')        

    cv.imwrite('C:/EPI_CONTROL/FACES/Face_' + cod + '.jpg' , face)

#Criar tela principal--------------------------------------------------------------------------------------------------------------------
tela_principal = tk.Tk(className='Webcam')
screen_width = tela_principal.winfo_screenwidth()
screen_width = (screen_width/2) - (500/2)
screen_height = tela_principal.winfo_screenheight()
screen_height = (screen_height/2) - (500/2)  

tela_principal.geometry('500x500+%d+%d' % (screen_width, screen_height)) #Tamanho
titulo=tk.Label(tela_principal, text='Controle de Entrega de EPI', font=('Terminal', '16', 'bold italic'))
loginButton = tk.Button(tela_principal, text="Movimento", command=lambda:tela_principal.quit(), height=1, width=20, border=10)
registerButton = tk.Button(tela_principal, text="Registro", command=lambda:telaRegistro(), height=1, width=20, border=10)
sobreButton = tk.Button(tela_principal, text="Sobre", command=lambda:telaSobre(),height=1, width=5, border=5)
loginButton.place(x=165, y=200)
registerButton.place(x=165, y=250)
sobreButton.place(x=450, y=470)
titulo.place(x=115, y=100)

tela_principal.mainloop() #Quero que ela fique rodando
