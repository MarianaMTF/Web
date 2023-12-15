def salvar(tasks):
  with open("arquivo_tarefas", "w")as arquivo:
    for tarefa in tasks:
      arquivo.write(f"{tarefa}\n")
