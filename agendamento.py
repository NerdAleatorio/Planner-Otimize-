import calendar

class Calendario:
  def __init__(self, dia, mes, hora, ano, diaSem):
    self.hora = hora
    self.dia = dia
    self.mes = mes
    self.ano = ano
    self.diaSem = diaSem

  def exibirCalendario(self):  
    aa = 2022
    mm = 10
    print(calendar.month(aa,mm))

  
class Agendamento:
  def __init__(self, descAgendamento):
    self.descAgendamento = descAgendamento
    self.calendario = Calendario('','','','','')

  





