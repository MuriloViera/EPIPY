import cv2 as cv #Precisa baixar
import tkinter as tk #Precisa baixar
from tkinter import *
from tkinter import messagebox
from tkinter import ttk as tkk
from PIL import Image, ImageTk #Precisa baixar
import os
import numpy as np #Precisa baixar provavelmente
import face_recognition

#Função tela info
def telaInfo(tela):
    tela_info = tk.Toplevel(tela_principal)
    screen_width = tela_info.winfo_screenwidth()
    screen_width = (screen_width/2) - (520/2)
    screen_height = tela_info.winfo_screenheight()
    screen_height = (screen_height/2) - (245/2)  
    tela_info.geometry('520x250+%d+%d' % (screen_width, screen_height)) #Tamanho
    tela_info.title('Info')
    if(tela == 0): #Tela mov
        text = "Informações sobre a movimentação:\n1) Informe nos campos a cima o seu código individual, codigo dos EPIS que deseja e ao lado a quantidade desse mesmo EPI.\n2) Tente posicionar sua face no centro do retangulo da camera deixando toda sua cabeça fique visivel.\n3) Se possivel remova óculos e bonés ou qualquer outro acessório que tampe ou esconda sua face.\n4) Por fim, olhe para a camera e clique no botão registrar ou enter no teclado sem desviar o olhar.\n5) Uma tela de confirmação aparece oficializando a movimentação casa não haja erro."
    elif(tela == 1): #Tela reg
        text = "Informações sobre o registro: \n1) Informe no campo a baixo o seu código individual.\n2) Tente posicionar sua face no centro do retangulo da camera de forma com que toda sua cabeça fique visivel.\n3) Se possivel remova óculos e bonés ou qualquer outro acessório que tampe ou esconda sua face.\n4) Por fim, olhe para a camera e clique no botão registrar ou enter no teclado sem desviar o olhar.\n5) Uma tela de confirmação aparecerá caso a operação de registro seja sucedida sem erros."
    informations = tk.Label(tela_info,justify=tk.LEFT,bd=2,wraplength='500',relief='solid',font=('Terminal', '16'),text=text)
    informations.place(x=5, y=5)

#Função tela movimentação
def telaMov():
    tela_principal.withdraw()
    tela_mov = tk.Toplevel(tela_principal)
    screen_width = tela_mov.winfo_screenwidth()
    screen_width = (screen_width/2) - (1050/2)
    screen_height = tela_mov.winfo_screenheight()
    screen_height = (screen_height/2) - (380/2)  
    tela_mov.geometry('975x375+%d+%d' % (screen_width, screen_height)) #Tamanho
    tela_mov.title('Movimentação')
    webcam = tk.Label(tela_mov, relief='solid', width=450, height=350)
    webcam.place(x=5, y=10)
    codLabel = tk.Label(tela_mov, font=('Terminal', '15'), text='Código de funcionário:')
    codLabel.place(x=490, y=10)
    cod = tk.Entry(tela_mov, width=10, font=('Terminal','15'))
    cod.place(x=720, y=13)
    listaEpis = ['8989 - Luvas', '8787 - Capacete', '9095 - Mascara']
    #listaEpis.append('9090 - Fone') Adicionar 1
    #listaEpis.extend('9090 - Fone', '8765 - Creme') Adicionar mais de 1

    codEpi1Label = tk.Label(tela_mov, font=('Terminal', '15'), text='Código do EPI:')
    codEpi1Label.place(x=490, y=55)
    epis1 = tkk.Combobox(tela_mov, values=listaEpis, font=('Terminal', '15'), width=30)
    epis1.place(x=635,y=55)

    codEpi2Label = tk.Label(tela_mov, font=('Terminal', '15'), text='Código do EPI:')
    codEpi2Label.place(x=490, y=105)
    epis2 = tkk.Combobox(tela_mov, values=listaEpis, font=('Terminal', '15'), width=30)
    epis2.place(x=635,y=105)

    codEpi3Label = tk.Label(tela_mov, font=('Terminal', '15'), text='Código do EPI:')
    codEpi3Label.place(x=490, y=155)
    epis3 = tkk.Combobox(tela_mov, values=listaEpis, font=('Terminal', '15'), width=30)
    epis3.place(x=635,y=155)

    codEpi4Label = tk.Label(tela_mov, font=('Terminal', '15'), text='Código do EPI:')
    codEpi4Label.place(x=490, y=205)
    epis1 = tkk.Combobox(tela_mov, values=listaEpis, font=('Terminal', '15'), width=30)
    epis1.place(x=635,y=205)

    codEpi5Label = tk.Label(tela_mov, font=('Terminal', '15'), text='Código do EPI:')
    codEpi5Label.place(x=490, y=255)
    epis5 = tkk.Combobox(tela_mov, values=listaEpis, font=('Terminal', '15'), width=30)
    epis5.place(x=635,y=255)

    #Botoes
    movimentarButton = tk.Button(tela_mov, text="Movimentar",state=DISABLED,font=('System','3'),height=2, width=15, border=10, activebackground='green')
    movimentarButton.place(x=750, y=300)
    registrarButton = tk.Button(tela_mov, text="Verificar",command=lambda:verificar(True),font=('System','3'),height=2, width=15, border=10, activebackground='green')
    registrarButton.place(x=580, y=300)
    infoButton = tk.Button(tela_mov, text="?", command=lambda:telaInfo(0) ,height=1,font=('System'),border=5)
    infoButton.place(x=948, y=340)
    
    #Função verificar
    def verificar(state):
        if(state):
            messagebox.showinfo("Sucesso", "Sua face foi verificada!")
            movimentarButton.config(state=NORMAL)
        else:
            messagebox.showerror("Erro", "Sua face não foi verificada!")
        
    #Acessar a camera
    camera = cv.VideoCapture(0)
    pegarFrames(camera,webcam)#Capturar os frames com a webcam

    tela_principal.wait_window(tela_mov)
    if(tk.Toplevel.winfo_exists(tela_mov) == 0):
        tela_principal.deiconify()

#Função tela sobre
def telaSobre():
    tela_principal.withdraw()
    tela_sobre = tk.Toplevel(tela_principal)
    screen_width = tela_sobre.winfo_screenwidth()
    screen_width = (screen_width/2) - (500/2)
    screen_height = tela_sobre.winfo_screenheight()
    screen_height = (screen_height/2) - (660/2)  
    tela_sobre.geometry('550x620+%d+%d' % (screen_width, screen_height)) #Tamanho
    tela_sobre.title('Sobre')
    info = tk.Label(tela_sobre,relief='solid',wraplength='550',font=('Terminal', '15'),text='Esse software foi desenvolvido para monitorar a saida de EPIs utilizando a tecnologia de reconhecimento' + 
    'facial, o mesmo funciona utilizando armazenamento local em sua versão atual. Seu funcionamento é simples, caso o usuário ainda' + 
    'não seja cadastrado basta clicar no botão REGISTRAR na tela principal e lá seguir as regras, após isso, caso o usuário deseje' + 
    'retirar um EPI, o mesmo necessita de fazer uma verificação clicando no botão MOVIMENTACAO e seguindo as informações de lá.' +
    'Todas essas informações são armazenadas em um diretório no disco raiz C:/ chamado de EPIPY_CONTROL, dentro dele existe, 3 ' + 
    'pastas uma com as faces registradas de cada usuário, uma com um arquivo csv de uma tabela com o nome o codigo de cada usuário' + 
    'cadastrado e a outra com um arquivo da mesma espécie que possui o dia, a hora, o nome/codigo e o tipo de epi retirado.')
    info.place(x=2, y=2)
    credit = tk.Label(tela_sobre,relief='solid',wraplength='550',font=('Terminal', '15'),text='Agradecimentos sinceros a Adam Geitgey por ter disponibilizado essa excelente biblioteca de reconhecimento facil que está disponível em: https://github.com/ageitgey/face_recognition, sem sua biblioteca o desenvolvimento desse software teria sido muito mais custosa e dolorosa')
    credit.place(x=2, y=320)
    contact = tk.Label(tela_sobre,padx=61,relief='solid',wraplength='550',font=('Terminal', '15'),text='Email para contato: contatoepipy@gmail.com')
    contact.place(x=2, y=440)
    crew = tk.Label(tela_sobre,padx=10,relief='solid',wraplength='550',font=('Terminal', '15'),text='Equipe do EPIPY \n Murilo Vieira Pizzamiglio - Desenvolvedor e criador da ferramenta \n murilo@pizzamiglio.eti.br - https://github.com/MuriloViera \n Carlos Cezar Pizzamiglio - Colaborador e gerente da ferramenta \n carlos@pizzamiglio.eti.br')
    crew.place(x=2, y=468)

    tela_principal.wait_window(tela_sobre)
    if(tk.Toplevel.winfo_exists(tela_sobre) == 0):
        tela_principal.deiconify()

#Função tela registro
def telaRegistro():
    #Configurações tela
    tela_principal.withdraw()
    tela_registro = tk.Toplevel(tela_principal)
    screen_width = tela_registro.winfo_screenwidth()
    screen_width = (screen_width/2) - (975/2)
    screen_height = tela_registro.winfo_screenheight()
    screen_height = (screen_height/2) - (375/2)  
    tela_registro.geometry('975x375+%d+%d' % (screen_width, screen_height)) #Tamanho
    tela_registro.title('Registro')

    #Webcam
    webcam = tk.Label(tela_registro, relief='solid', width=450, height=350)
    webcam.place(x=5, y=10)

    #Linha codigo
    cod = tk.Entry(tela_registro, width=10, font=('Terminal', '15'))
    cod.place(x=595, y=120)
    codLabel = tk.Label(tela_registro, font=('System', '17', 'bold'), text='Código:')
    codLabel.place(x=490, y=110)

    #Linha nome
    name = tk.Entry(tela_registro, width=33, font=('Terminal', '15'))
    name.place(x=580,y=165)
    nameLabel = tk.Label(tela_registro, font=('System', '17', 'bold'), text='Nome:')
    nameLabel.place(x=490, y=155)

    #Botao
    registrarButton = tk.Button(tela_registro, text="Registrar",font=('System','3'), command=lambda: registrar(cod, camera, tela_registro, name) ,height=1, width=15, border=10, activebackground='green')
    registrarButton.place(x=650, y=220)
    infoButton = tk.Button(tela_registro, text="?", command=lambda:telaInfo(1) ,height=1,font=('System'),border=5)
    infoButton.place(x=948, y=340)
    
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
def registrar(cod,camera, tela_registro, name):
    cod = cod.get() #Aqui to recebendo o que tem no campo cod
    name = name.get() #Aqui to recebendo o que tem no campo name

    if((cod.isdigit()) and (all(n.isalpha() for n in name.split(" ")))):
        if(len(cod) <= 10):
            ret, face = camera.read() #Aqui to pegando 1 frame no momento em que o cara clicar no register
        
            if(os.path.exists('C:/EPIPY_CONTROL/FACES') == False):
                os.makedirs('C:/EPIPY_CONTROL/FACES')

            if(os.path.exists('C:/EPIPY_CONTROL/REGISTRO') == False):
                os.makedirs('C:/EPIPY_CONTROL/REGISTRO')

            if(os.path.exists('C:/EPIPY_CONTROL/MOVIMENTACAO') == False):
                os.makedirs('C:/EPIPY_CONTROL/MOVIMENTACAO')

            kernel = np.ones((2,2),np.uint8)
        
            faceFinal = cv.medianBlur(face, 1)  
            faceFinal = cv.morphologyEx(faceFinal,cv.MORPH_CLOSE, kernel, iterations=1)
            faceFinal = faceFinal[65:350+65 ,95:450+95]
            cv.imwrite('C:/EPIPY_CONTROL/FACES/Face_' + cod + '.jpg' , faceFinal)
            messagebox.showinfo("Sucesso", "Seu registro foi efetuado com sucesso!")
            tela_registro.destroy()
        else:
           messagebox.showerror("Erro", "Por favor, verifique o seu código e o escreva novamente certificando de que a quantidade de números esteja correta!")     
    else:
        messagebox.showerror("Erro", "Por favor, verifique o seu código ou nome e os escreva novamente certificando de que existem apenas elementos numéricos no campo código e apenas letras no campo nome!")

#Criar tela principal--------------------------------------------------------------------------------------------------------------------
tela_principal = tk.Tk(className='Webcam')
screen_width = tela_principal.winfo_screenwidth()
screen_width = (screen_width/2) - (500/2)
screen_height = tela_principal.winfo_screenheight()
screen_height = (screen_height/2) - (500/2)  

tela_principal.geometry('500x500+%d+%d' % (screen_width, screen_height)) #Tamanho
titulo=tk.Label(tela_principal, text='Controle de Entrega de EPI', font=('Terminal', '16', 'bold italic'))
loginButton = tk.Button(tela_principal,font=('System','3'), text="Movimento", command=lambda:telaMov(), height=1, width=20, border=10)
registerButton = tk.Button(tela_principal,font=('System','3') ,text="Registro", command=lambda:telaRegistro(), height=1, width=20, border=10)
sobreButton = tk.Button(tela_principal, font=('System','3'),text="Sobre", command=lambda:telaSobre(),height=1, width=5, border=5)
loginButton.place(x=165, y=200)
registerButton.place(x=165, y=250)
sobreButton.place(x=440, y=462)
titulo.place(x=115, y=100)
version=tk.Label(tela_principal, text='Versão 1.0.0', font=('Terminal', '10', 'bold italic'))
version.place(x=5, y=480)
epiButton = tk.Button(tela_principal,font=('System','3') ,text="Cadastrar EPI", height=1, width=20, border=10)
epiButton.place(x=165, y=300)
tela_principal.mainloop() #Quero que ela fique rodando
