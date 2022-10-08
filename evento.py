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

        os.system("clear")

    
  def editarEvento(self):
        print()

    
  def consultarEvento(self):
        from usuario import solicitarID
        print("Eventos localizados: \n")

        with open('./bdAtividades/bdUsuario' + str(solicitarID) + '/atvUsuario' + str(solicitarID) + '.txt', 'r') as file:
          line = file.readlines()

        print("Evento: {}Data: {}Hora: {}Local: {}".format(line[0], line[1], line[2], line[3]))
  
        
  def excluirEvento(self):
        from usuario import solicitarID
   
        delArquivo = input("\nSelecione o evento a ser excluído: ")
  
        for diretorio, subpastas, arquivos in os.walk("bdAtividades/bdUsuario" + str(solicitarID)):
          for arquivo in arquivos:
            os.remove("./bdAtividades/bdUsuario" + str(solicitarID) + "/atvUsuario" + str(delArquivo) + ".txt")
  
        print("Evento excluído.")
    