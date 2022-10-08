import os
from usuario import*


class Evento:
  def __init__(self, nomeEvento, dataEvento, horaEvento, prioridadeEvento, localEvento):
      self.nomeEvento = nomeEvento
      self.dataEvento = dataEvento
      self.horaEvento = horaEvento
      self.prioridadeEvento = prioridadeEvento
      self.localEvento = localEvento

  def adicionarEvento(self):
        from usuario import solicitarID

        if not os.path.exists('./bdAtividades/bdUsuario' + str(solicitarID)):
          os.mkdir('./bdAtividades/bdUsuario' + str(solicitarID))
        else:
          pass
 
        self.nomeEvento = input("Nome do Evento: ")
        self.dataEvento = input("Data do Evento: ")
        self.horaEvento = input("Hora do Evento: ")
        self.localEvento = input("Local do Evento: ")
        
        with open('./bdAtividades/bdUsuario' + str(solicitarID) + '/atvUsuario' + str(solicitarID) + '.txt', 'a') as file:
          file.write(self.nomeEvento + "\n" + self.dataEvento + "\n" + self.horaEvento + "\n" + self.localEvento)
          file.seek(0,0)
          file.close()

        

    
  def editarEvento(self):
        print()

    
  def consultarEvento(self):
        from usuario import solicitarID
        print("Eventos localizados: \n")

        with open('./bdAtividades/bdUsuario' + str(solicitarID) + '/atvUsuario' + str(solicitarID) + '.txt', 'r') as file:
          line = file.readlines()

        print("Evento: {}Data: {}Hora: {}Local: {}Prioridade: {}".format(line[0], line[1], line[2], line[3], line[4]))
  
        
  def excluirEvento(self):
        from usuario import solicitarID
   
        delArquivo = input("\nSelecione o evento a ser excluído: ")
  
        for diretorio, subpastas, arquivos in os.walk("bdAtividades/bdUsuario" + str(solicitarID)):
          for arquivo in arquivos:
            os.remove("./bdAtividades/bdUsuario" + str(solicitarID) + "/atvUsuario" + str(delArquivo) + ".txt")
  
        print("Evento excluído.")

  def definirPrioridade(self):
    from usuario import solicitarID

    print("Determine o nível de prioridade do  seu evento: \n")
    prioridade = int(input("1.Baixa \n2.Moderada \n3.Elevada \n4.Absoluta \n----> "))
    
    if prioridade == 1:
      self.prioridadeEvento = "Baixa"

    elif prioridade == 2:
      self.prioridadeEvento = "Moderada"

    elif prioridade == 3:
      self.prioridadeEvento = "Elevada"

    elif prioridade == 4:
      self.prioridadeEvento = "Absoluta"

    
    with open('./bdAtividades/bdUsuario' + str(solicitarID) + '/atvUsuario' + str(solicitarID) + '.txt', 'a') as file:
              file.write("\n" + self.prioridadeEvento)
              file.seek(0,0)
              file.close()