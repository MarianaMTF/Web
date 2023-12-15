def excluir(tasks):
  with open("arquivo_tarefas.txt", "w")as arquivo:
    for tarefa in tasks:
      arquivo.write(f"{tarefa}\n")
