import cv2 as cv #Precisa baixar
import tkinter as tk #Precisa baixar
import sqlite3
from tkinter import * 
from tkinter import messagebox
from tkinter import ttk as tkk
from PIL import Image, ImageTk #Precisa baixar
import os
import numpy as np #Precisa baixar provavelmente
import face_recognition
from datetime import datetime

#FUNÇÕES DE TELA

def telaRegEpi():
    tela_regepi = tk.Toplevel(tela_principal)
    screen_width = tela_regepi.winfo_screenwidth()
    screen_width = (screen_width/2) - (520/2)
    screen_height = tela_regepi.winfo_screenheight()
    screen_height = (screen_height/2) - (245/2)  
    tela_regepi.geometry('520x250+%d+%d' % (screen_width, screen_height)) #Tamanho
    tela_regepi.title('Registrar EPI')
    tela_regepi.resizable(0,0)

    codEpi = tk.Entry(tela_regepi,validate='key',validatecommand=(valNum, '%S'),width=15, font=('Terminal', '15'))
    codEpi.place(x=152, y=65)
    codEpiLabel = tk.Label(tela_regepi, font=('Terminal', '17'), text='Código do EPI:')
    codEpiLabel.place(x=5, y=65)

    codCA = tk.Entry(tela_regepi,validate='key',validatecommand=(valNum, '%S'),width=15, font=('Terminal', '15'))
    codCA.place(x=115, y=5)
    codCALabel = tk.Label(tela_regepi, font=('Terminal', '17'), text='Código CA:')
    codCALabel.place(x=5, y=5)

    dateCADay = tk.Entry(tela_regepi,validate='key',validatecommand=(valNum, '%S'),width=2, font=('Terminal', '15'))
    dateCADay.place(x=165, y=35)
    bar = tk.Label(tela_regepi, font=('Terminal', '17'), text='/')
    bar.place(x=190, y=35)
    dateCAMonth = tk.Entry(tela_regepi,validate='key',validatecommand=(valNum, '%S'),width=2, font=('Terminal', '15'))
    dateCAMonth.place(x=205, y=35)
    bar = tk.Label(tela_regepi, font=('Terminal', '17'), text='/')
    bar.place(x=230, y=35)
    dateCAYear = tk.Entry(tela_regepi,validate='key',validatecommand=(valNum, '%S'),width=4, font=('Terminal', '15'))
    dateCAYear.place(x=245, y=35)
    dateCALabel = tk.Label(tela_regepi, font=('Terminal', '17'), text='Validade do CA:')
    dateCALabel.place(x=5, y=35)

    desc = tk.Entry(tela_regepi,width=15, font=('Terminal', '15'))
    desc.place(x=185, y=95)
    codCALabel = tk.Label(tela_regepi, font=('Terminal', '17'), text='Descrição do EPI:')
    codCALabel.place(x=5, y=95)


#Função tela info
def telaInfo(tela):
    tela_info = tk.Toplevel(tela_principal)
    screen_width = tela_info.winfo_screenwidth()
    screen_width = (screen_width/2) - (520/2)
    screen_height = tela_info.winfo_screenheight()
    screen_height = (screen_height/2) - (245/2)  
    tela_info.geometry('520x250+%d+%d' % (screen_width, screen_height)) #Tamanho
    tela_info.title('Info')
    tela_info.resizable(0,0)
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
    tela_mov.resizable(0,0)
    webcam = tk.Label(tela_mov, relief='solid', width=450, height=350)
    webcam.place(x=5, y=10)

    codLabel = tk.Label(tela_mov, font=('Terminal', '15'), text='Código de funcionário:')
    codLabel.place(x=490, y=10)
    codentry = tk.Entry(tela_mov,validate='key',validatecommand=(valNum, '%S'), width=10, font=('Terminal','15'))
    codentry.place(x=720, y=13)

    listaEpis = ['8989-Luvas', '8787-Capacete', '9095-Mascara']
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
    epis4 = tkk.Combobox(tela_mov, values=listaEpis, font=('Terminal', '15'), width=30)
    epis4.place(x=635,y=205)

    codEpi5Label = tk.Label(tela_mov, font=('Terminal', '15'), text='Código do EPI:')
    codEpi5Label.place(x=490, y=255)
    epis5 = tkk.Combobox(tela_mov, values=listaEpis, font=('Terminal', '15'), width=30)
    epis5.place(x=635,y=255)

    #Botoes
    movimentarButton = tk.Button(tela_mov, text="Movimentar",command=lambda:movimentar(codentry, epis1, epis2, epis3, epis4, epis5),state=DISABLED,font=('System','3'),height=2, width=15, border=10, activebackground='green')
    movimentarButton.place(x=750, y=300)
    registrarButton = tk.Button(tela_mov, text="Verificar",command=lambda:verificar(codentry),font=('System','3'),height=2, width=15, border=10, activebackground='green')
    registrarButton.place(x=580, y=300)
    infoButton = tk.Button(tela_mov, text="?", command=lambda:telaInfo(0) ,height=1,font=('System'),border=5)
    infoButton.place(x=948, y=340)
    
    #Função movimentar
    def movimentar(cod, epi1cbox, epi2cbox, epi3cbox, epi4cbox, epi5cbox):
        cod = cod.get()
        datahora = datetime.now()
        datahora = datahora.strftime("%d/%m/%Y %H:%M")
        datahora = datahora.split()
    
        epi1 = epi1cbox.get()
        epi1 = epi1.split('-')
        epi2 = epi2cbox.get()
        epi2 = epi2.split('-')
        epi3 = epi3cbox.get()
        epi3 = epi3.split('-')
        epi4 = epi4cbox.get()
        epi4 = epi4.split('-')
        epi5 = epi5cbox.get()
        epi5 = epi5.split('-')
     
        banco = sqlite3.connect('C:/EPIPY_CONTROL/REGISTRO/banco_Sqlite.db')
        cursor = banco.cursor()
        
        if epi1[0] != '':
            cursor.execute("INSERT INTO MOVIMENTACAO (cod, codEpi, data, horario) VALUES(?, ?, ?, ?)", (cod, epi1[0], datahora[0], datahora[1]))
        if epi2[0] != '':
            cursor.execute("INSERT INTO MOVIMENTACAO (cod, codEpi, data, horario) VALUES(?, ?, ?, ?)", (cod, epi2[0], datahora[0], datahora[1]))
        if epi3[0] != '':
            cursor.execute("INSERT INTO MOVIMENTACAO (cod, codEpi, data, horario) VALUES(?, ?, ?, ?)", (cod, epi3[0], datahora[0], datahora[1]))    
        if epi4[0] != '':
            cursor.execute("INSERT INTO MOVIMENTACAO (cod, codEpi, data, horario) VALUES(?, ?, ?, ?)", (cod, epi4[0], datahora[0], datahora[1]))
        if epi5[0] != '':
            cursor.execute("INSERT INTO MOVIMENTACAO (cod, codEpi, data, horario) VALUES(?, ?, ?, ?)", (cod, epi5[0], datahora[0], datahora[1]))    

        banco.commit()

        messagebox.showinfo("Sucesso", "Movimentação realizada com sucesso")
        tela_mov.destroy()
        
    #Função verificar
    def verificar(cod):
        cod = cod.get()
        ret, face = camera.read()
    
        if os.path.exists('C:/EPIPY_CONTROL/FACES/Face_' + cod + '.jpg' ):

            faceRegistrada = cv.imread('C:/EPIPY_CONTROL/FACES/Face_' + cod + '.jpg')
            faceRegistrada = cv.cvtColor(faceRegistrada, cv.COLOR_BGR2RGB)
            faceRegCod = face_recognition.face_encodings(faceRegistrada, num_jitters=10)

            faceAtual = face[65:350+65 ,95:450+95]
            faceActCod = face_recognition.face_encodings(faceAtual)
        
            if len(faceRegCod) and len(faceActCod) > 0:
                faceRegCod = faceRegCod[0]
                faceActCod = faceActCod[0]

                result = face_recognition.compare_faces([faceRegCod], faceActCod, tolerance=0.5)

                if(result[0]):
                    messagebox.showinfo("Sucesso", "Sua face foi verificada!")
                    movimentarButton.config(state=NORMAL)
                    codentry.config(state = DISABLED)
                else:
                    messagebox.showerror("Erro", "Sua face não foi verificada!")

            else:
                messagebox.showerror("Erro", "Sua face não foi encontrada!")    
             
        else:
            messagebox.showerror("Erro", "Sua face não está cadastrada!")
        
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
    tela_sobre.resizable(0,0)

    tela_principal.wait_window(tela_sobre)
    if(tk.Toplevel.winfo_exists(tela_sobre) == 0):
        tela_principal.deiconify()

#Função tela registro
def telaRegistro():
    #Configurações tela
    tela_principal.withdraw()
    tela_registro = tk.Toplevel(tela_principal)
    screen_width = tela_registro.winfo_screenwidth()
    screen_width = (screen_width/2) - (465/2)
    screen_height = tela_registro.winfo_screenheight()
    screen_height = (screen_height/2) - (550/2)  
    tela_registro.geometry('465x550+%d+%d' % (screen_width, screen_height)) #Tamanho
    tela_registro.title('Registro')
    tela_registro.resizable(0,0)

    #Webcam
    webcam = tk.Label(tela_registro, relief='solid', width=450, height=350)
    webcam.place(x=5, y=10)

    #Linha codigo
    cod = tk.Entry(tela_registro,validate='key',validatecommand=(valNum,6, '%S'),width=31, font=('Terminal', '15'))
    cod.place(x=115, y=383)
    codLabel = tk.Label(tela_registro, font=('Terminal', '17'), text='Código:')
    codLabel.place(x=35, y=380)

    #Linha nome
    name = tk.Entry(tela_registro, validate='key', validatecommand=(valCha, '%S'),width=33, font=('Terminal', '15'))
    name.place(x=95,y=425)
    nameLabel = tk.Label(tela_registro, font=('Terminal', '17'), text='Nome:')
    nameLabel.place(x=35, y=422.5)

    #Botao
    registrarButton = tk.Button(tela_registro, text="Registrar",font=('System','3'), command=lambda: registrar(cod, camera, tela_registro, name) ,height=1, width=15, border=10, activebackground='green')
    registrarButton.place(x=160, y=470)
    infoButton = tk.Button(tela_registro, text="?", command=lambda:telaInfo(1) ,height=1,font=('System'),border=5)
    infoButton.place(x=438, y=515)
    
    #Acessar a camera
    camera = cv.VideoCapture(0)
    pegarFrames(camera,webcam)#Capturar os frames com a webcam

    tela_principal.wait_window(tela_registro)
    if(tk.Toplevel.winfo_exists(tela_registro) == 0):
        tela_principal.deiconify()


#FUNÇÕES VARIADAS

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

    if(len(cod) <= 10):
        ret, face = camera.read() #Aqui to pegando 1 frame no momento em que o cara clicar no register

        kernel = np.ones((2,2),np.uint8)
        
        faceFinal = cv.medianBlur(face, 1)  
        faceFinal = cv.morphologyEx(faceFinal,cv.MORPH_CLOSE, kernel, iterations=1)
        faceFinal = faceFinal[65:350+65 ,95:450+95]
        cv.imwrite('C:/EPIPY_CONTROL/FACES/Face_' + cod + '.jpg' , faceFinal)

        banco = sqlite3.connect('C:/EPIPY_CONTROL/REGISTRO/banco_Sqlite.db')
        cursor = banco.cursor()
        cursor.execute("INSERT INTO REGISTRO (cod, nome) VALUES(?, ?)", (cod, name))
        banco.commit()

        messagebox.showinfo("Sucesso", "Seu registro foi efetuado com sucesso!")
        tela_registro.destroy()
    else:
        messagebox.showerror("Erro", "Por favor, verifique o seu código e o escreva novamente certificando de que a quantidade de números esteja correta!")     

#Função para validar digitos
def numeros(char):
    return char.isdigit()
    
#Função para validar letras
def letras(char):
    return all(chr.isalpha() or chr.isspace() for chr in char)   

#INICIO DO CODIGO RAIZ DO PROGRAMA

#Criação das pastas
if(os.path.exists('C:/EPIPY_CONTROL/FACES') == False):
    os.makedirs('C:/EPIPY_CONTROL/FACES')

    if(os.path.exists('C:/EPIPY_CONTROL/REGISTROS') == False):
        os.makedirs('C:/EPIPY_CONTROL/REGISTRO')

        #Criar banco e criar as tabelas
        banco = sqlite3.connect('C:/EPIPY_CONTROL/REGISTRO/banco_Sqlite.db')

        cursor = banco.cursor()

        cursor.execute('CREATE TABLE REGISTRO (cod integer, nome text, PRIMARY KEY (cod))')
        cursor.execute('CREATE TABLE MOVIMENTACAO (cod integer, codEpi integer, data text, horario text)')
        cursor.execute('CREATE TABLE EPIS (nome text, idade integer, email text)')
 
        banco.commit()

#Criar tela principal
tela_principal = tk.Tk(className='Epipy')
screen_width = tela_principal.winfo_screenwidth()
screen_width = (screen_width/2) - (500/2)
screen_height = tela_principal.winfo_screenheight()
screen_height = (screen_height/2) - (500/2)  

#Vai caraio
#icone = PhotoImage(file='icon.png')
#tela_principal.iconphoto(True,icone)

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
epiButton = tk.Button(tela_principal,font=('System','3') ,command=lambda:telaRegEpi(),text="Cadastrar EPI", height=1, width=20, border=10)
epiButton.place(x=165, y=300)
tela_principal.resizable(0,0)

valNum = tela_principal.register(numeros) 
valCha = tela_principal.register(letras) 

tela_principal.mainloop() 
