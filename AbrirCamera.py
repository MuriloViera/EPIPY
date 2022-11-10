import cv2 as cv #Precisa baixar
import tkinter as tk #Precisa baixar
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk #Precisa baixar
import os
import numpy as np #Precisa baixar provavelmente

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
    tela_principal.withdraw()
    tela_registro = tk.Toplevel(tela_principal)
    screen_width = tela_registro.winfo_screenwidth()
    screen_width = (screen_width/2) - (1000/2)
    screen_height = tela_registro.winfo_screenheight()
    screen_height = (screen_height/2) - (500/2)  
    tela_registro.geometry('1055x500+%d+%d' % (screen_width, screen_height)) #Tamanho
    tela_registro.title('Registro')
    webcam = tk.Label(tela_registro, relief='solid')
    webcam.place(x=2, y=10)
    cod = tk.Entry(tela_registro, width=10, font=('30'))
    cod.place(x=755, y=335)
    name = tk.Entry(tela_registro, width=33, font=('20'))
    name.place(x=740, y=375)
    registrarButton = tk.Button(tela_registro, text="Registrar",font=('System','3'), command=lambda: registrar(cod, camera, tela_registro, name) ,height=1, width=15, border=10, activebackground='green')
    registrarButton.place(x=770, y=420)
    informations = tk.Label(tela_registro,justify=tk.CENTER,bd=2,relief='solid',wraplength=400,font=('Terminal', '16'),text="Informações: \n 1) Informe no campo a baixo o seu código individual \n 2) Tente posicionar sua face no centro do retangulo da camera de forma com que toda sua cabeça fique visivel \n 3) Se possivel remova óculos e bonés ou qualquer outro acessório que tampe ou esconda sua face \n 4) Por fim, olhe para a camera e clique no botão registrar ou enter no teclado sem desviar o olhar \n 5) Caso sua face seja registrada uma mensagem aparecerá na tela, caso algum erro ocorra uma janela de informações sobre o erro também aparecerá")
    informations.place(x=650, y=10)
    codLabel = tk.Label(tela_registro, font=('System', '17', 'bold'), text='Código:')
    codLabel.place(x=650, y=325)
    nameLabel = tk.Label(tela_registro, font=('System', '17', 'bold'), text='Nome:')
    nameLabel.place(x=650, y=365)

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
loginButton = tk.Button(tela_principal,font=('System','3'), text="Movimento", command=lambda:tela_principal.quit(), height=1, width=20, border=10)
registerButton = tk.Button(tela_principal,font=('System','3') ,text="Registro", command=lambda:telaRegistro(), height=1, width=20, border=10)
sobreButton = tk.Button(tela_principal, font=('System','3'),text="Sobre", command=lambda:telaSobre(),height=1, width=5, border=5)
loginButton.place(x=165, y=200)
registerButton.place(x=165, y=250)
sobreButton.place(x=440, y=462)
titulo.place(x=115, y=100)

tela_principal.mainloop() #Quero que ela fique rodando
