#Chute um número
import random

class chute_um_numero:
  def __init__(self):
    self.valor_aleatorio = 0
    self.valor_minimo = 1
    self.valor_maximo = 100
    self.tentar_novamente = True

  def Iniciar(self):
    self.gerar_numero_aleatorio()
    self.pedir_valor_aleatorio()
    while self.tentar_novamente == True:
    
      if int(self.valor_do_chute) > self.valor_aleatorio:
        print('chutou alto, escolha um número menor')
        self.pedir_valor_aleatorio()
      elif int(self.valor_do_chute) < self.valor_aleatorio:
        print('chutou baixo, escolha um número maior')
        self.pedir_valor_aleatorio()
      if int(self.valor_do_chute) == self.valor_aleatorio:
        self.tentar_novamente = False
        print('parabéns, voce acertou o número!!!!!!')

  def pedir_valor_aleatorio(self):
    self.valor_do_chute = input('chute um número:')
    
  def gerar_numero_aleatorio(self):
    self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)

chute = chute_um_numero()
chute.Iniciar()
