#PLANNER OTIMIZE+ - 2° INFORMÁTICA VESPERTINO
#Desenvolvedores: Ana Beatriz Pimenta e Ian Vinícius Vasconcelos

from agendamento import*
from usuario import*
from evento import*


import os
import time
import pathlib

#MENU INICIAL OTIMIZE+ - PRÉ LOGIN
def menu():
      print('\033[1;49;95mPLANNER OTIMIZE+\033[m')
      print('\n1.EFETUAR CADASTRO\n2.EFETUAR LOGIN\n3.SOBRE OTIMIZE+')
  
  
      escolha = int(input('\n----> '))
  
      if escolha == 1:
          user.cadUsuario()
          os.system("clear")
        
          from usuario import contador
          print('\033[1;49;34mUSUÁRIO CADASTRADO.\033[m')
          print('\033[0;49;34mID DE LOGIN: {}\n\033[m'.format(contador+1))
          
          
          menu()
        
      elif escolha == 2:
          user.efetuarLogin()
          from usuario import verificacao
        
          if verificacao == True:
            print('\033[1;49;34mBEM VINDO!\033[m')
            wait()
            planner()
  
          elif verificacao == False:
            os.system("clear")
            print('\033[0;49;31mSenha inválida. Tente novamente.\033[m')
            menu()
    
      elif escolha == 3:
          os.system("clear")
          print('\033[1;49;95mOTIMIZE+\033[m')
        
          print('\033[1;49;34m\nO projeto Otimize+ foi criado para auxiliar e acompanhar seus usuários no dia a dia, facilitando a organização e identificação de atividades em geral.\033[m')
  
          print('\033[1;49;34m\nIdealizado por seus desenvolvedores no ano de 2022 durante o período da avaliação multidisciplinar conhecida como Projeto Integrador, no Instituto Federal de Educação, Ciência e Tecnologia de Rondônia. Inteiramente autoral, desde sua documentação, lógica e código, baseada em estudos e atividades realizadas pelos criadores, sendo tudo isso possível graças ao esforço de seus mentores.\033[m')
        
          print('\033[1;49;96m\n\nDesenvolvedores:\033[m')
  
          print('\033[0;49;36mAna Beatriz Pimenta - @bia_pimenta12 \nIan Vinícius Vasconcelos - @uianviniciuz\033[m')
  
          print('\033[1;49;96m\n\nMentores:\033[m')
  
          print('\033[0;49;36mDaniela Tissuya Silva Toda\nElisângela Bibá Gomes\nCamila Serrão\nAugustin Cantai\033[m')
          
          print('\033[1;49;90m\n\nEste projeto não possui objetivos comerciais, sendo completamente desenvolvido para fins de aprendizagem.\033[m')
        
          print('\033[1;49;90m\nOtimize+™ todos os direitos reservados.\n\n\033[m')
          
          returning()
        
      elif escolha > 3:    
        raise Exception("Opção inválida.")
        
  

#MENU INICIAL DO PLANNER - PÓS LOGIN
def planner():
  conectado()
  print("1. MOSTRAR EVENTOS\n2. ADICIONAR EVENTO\n3. REMOVER EVENTO\n4. CONTA")

  quest = int(input("\n----> "))

  if quest == 1:
      os.system("clear")
      conectado()
      verificarArq()

      if contar == 0:
        os.system("clear")
        conectado()
        print("Não há eventos agendados.")
        comeBack()
        
      else:
        evento.consultarEvento()
        comeBack()
    
    
  elif quest == 2:
      os.system("clear")
      conectado()
      evento.adicionarEvento()
      evento.definirPrioridade()
      os.system("clear")
      planner()

    
  elif quest == 3:
      os.system("clear")
      conectado()
    
      verificarArq()
      if contar == 0:
        os.system("clear")
        conectado()
        print("Não há eventos agendados.")
        comeBack()
        
      else:
        print('\033[0;49;34mDigite o N° do evento de acordo com a ordem abaixo: \033[m')
        evento.consultarEvento()
        evento.excluirEvento()
        comeBack()   
        
  elif quest == 4:
      os.system("clear")
      conectado()
      user.consultarUsuario()
    
      print("\nx - Excluir usuário \nENTER - Retornar ao menu")
      opcoes = input("----> ")

      if opcoes == "x":
        from usuario import confirm
        user.excluirUsuario()
        
        if confirm == True:
          os.system("clear")
          menu()
          
        elif confirm == False:
          os.system("clear")
          planner()
        
      elif opcoes == "":
        os.system("clear")
        planner()
  
  elif quest == 5:
      os.system("clear")
      conectado()
      calen.exibirCalendario()
    
  
#VERIFICAÇÃO DE EXISTÊNCIA DE ARQUIVOS
def verificarArq():
  global contar
  contar = 0
  from usuario import solicitarID

  for file in pathlib.Path("./bdAtividades/bdUsuario" + str(solicitarID)).iterdir():
      if file.is_file():
          contar += 1

  if contar == 0:
    print("Eventos não encontrados.")
    
  else:
    pass
    
#QUAL USUÁRIO ESTÁ UTILIZANDO O PLANNER?    
def conectado():
  from usuario import conectado
  print('\033[1;49;95mPLANNER OTIMIZE+\033[m')
  print('\033[0;49;36mCONECTADO COMO: {}\033[m'.format(conectado))


#CRIAÇÃO DO BANCO DE DADOS - USUÁRIOS
def BD():
  if not os.path.exists('bd'):
    os.makedirs('bd')
  else:
    pass


#CRIAÇÃO DO BANCO DE DADOS - ATIVIDADES
def bdAtividades():
  if not os.path.exists('bdAtividades'):
    os.makedirs('bdAtividades')
  else:
    pass

    
#FUNÇÃO AUXILIAR DECORATIVA
def wait():
  var = "\nCarregando..."
  
  for perae in var:
    time.sleep(0.15)
    print(perae, end = '', flush = True )  

  os.system("clear")


#FUNÇÕES AUXILIARES UTILITÁRIAS
def comeBack():
  ask = input("\nENTER - Voltar ao menu\n----> ")
  if ask == "":
    os.system("clear")
    planner()
  else:
    pass

def returning():
  ask = input("\nENTER - Voltar ao menu ")
  if ask == "":
    os.system("clear")
    menu()
  else:
    pass
    
#OBJETOS
user = Usuario(0,0,0,0)  
evento = Evento(0,0,0,0,0)
calen = Calendario(0,0,0,0,0)

#INICIAR
BD()
bdAtividades()
menu()

