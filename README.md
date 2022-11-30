<p align="center">
  <img src="https://user-images.githubusercontent.com/79518797/204881975-05c356b8-b684-4310-9ebd-16227bc8ed11.png"/>
</p>


<h1 align='center'>EPIPY</h1>

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/Git-E34F26?style=for-the-badge&logo=git&logoColor=white"/> <img src="https://img.shields.io/badge/-OpenCV-%235C3EE8?style=for-the-badge&logo=opencv&logoColor=white"/> <img src="https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white"/>
</p>

# Visão geral
> Esta ferramenta trata-se de uma aplicação python para controlar por meio de reconhecimento facial a entrada e saida de EPIS de uma industria/usina. Isso funciona utilizando a biblioteza Facerecognition e Opencv e SQLite3 para guardar as imagens em forma de banco de dados.

# Informações
>Esta aplicação salva os usuários, epis e movimentação em tabelas SQL no arquivo .db criado pelo mesmo, e as fotos em uma pasta no mesmo diretório criado. Em seu princípio a ferramenta possui 3 telas:
>>Registro:
>>Nesta tela o usuário insere seu nome e codigo, e retira sua foto que será sua face principal de seu cadastro, aquela usada para comparações faciais futuras.
>
>>Movimento:
>>Aqui o usuário necessita-se de tirar uma foto atual, e ser verificado baseado na sua face original de cadastro, caso a verificação facial seja validada, ele podera retirar os EPIS que necessita.
>
>>Cadastro EPI:
>>Nesta tela cadastra-se os EPIS que estão disponíveis para os funcinários retirarem.
>

