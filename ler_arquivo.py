def ler():
  with open("arquivo_tarefas.txt", "r")as arquivo:
    return arquivo.readlines()
