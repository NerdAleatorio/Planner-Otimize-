import os
import pathlib
from evento import*


global confirm
confirm = False

usuarios = {}

class Usuario():
  def __init__(self, nome, email, senha, ID):
    self.nome = nome
    self.email = email
    self.senha = senha
    self.ID = ID


  def getEmail(self):
    return self.email

  def getSenha(self):
    return self.senha

    
  def cadUsuario(self):
    self.nome = input('Insira seu nome: ')
    self.email = input('Insira seu email: ')
    self.senha = input('Utilize apenas números. Insira sua senha: ')

    global contador
    contador = 0
    for arquivo in pathlib.Path("bd").iterdir():
      if arquivo.is_file():
          contador += 1
        
      else:
        pass

    self.ID = contador + 1
      
    with open('./bd/Usuario' + str(contador + 1) + '.txt', 'a') as file:
      file.write(str(self.ID) + '\n' + self.nome + '\n' + self.email + '\n' + self.senha)
      file.seek(0,0)
      file.close()

  
  def efetuarLogin(self): 
      global verificacao
      global solicitarID

      solicitarID = input("Insira seu ID: ")
      solicitarSenha = input("Insira sua senha: ")
    
      with open('./bd/Usuario' + str(solicitarID) + '.txt', 'r') as file:
        linha = file.readlines()
      
      if solicitarSenha == linha[3]:
        verificacao = True
        
      else:
        verificacao = False

      
      file.close()
        
      global conectado
      conectado = linha[1]

  
  def consultarUsuario(self):
      with open('./bd/Usuario' + str(solicitarID) + '.txt', 'r') as file:
        line = file.readlines()

      print("Informações do usuário: \n")
      print("Nome: {}Email: {} \nSenha: {} \nID de usuário: {}".format(line[1], line[2], line[3], line[0]))
        

  def excluirUsuario(self):  
        print("\n\nExcluir permanentemente sua conta? \n1.SIM / 2.NÃO")
        try:
          confirmar = int(input("----> "))
        
          if confirmar == 1:
            confirm = True
            os.remove('./bd/Usuario' + str(solicitarID) + '.txt')
            os.remove('./bdAtividades/bdUsuario' + str(solicitarID) + '/atvUsuario' + str(solicitarID) + '.txt')
            
          elif confirmar == 2:
            confirm = False
            pass

        except ValueError:
          print("Digite apenas inteiros.")
          