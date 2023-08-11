

from random import randint
def numero_aleatorio():
  aleatorio=randint(1,10)
  chute=0
  while aleatorio != chute:
    chute=int(input("Coloque um número (1 a 10): "))
    if (aleatorio == chute):
      print("Coisa boa. Você ACERTOUUU!")
    else:
      print("errou meu parceiro, tente novamente.")
numero_aleatorio()
