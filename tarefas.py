# Lista que armazenará as tarefas
tarefas = []

def adicionar_tarefa(nome):
    tarefa = {
        "nome": nome,
        "concluida": False
    }
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\nLista de Tarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["concluida"] else " "
        print(f"{i}. [{status}] {tarefa['nome']}")

def marcar_concluida(indice):
    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True
        print("Tarefa marcada como concluída!")
    else:
        print("Índice inválido.")

def remover_tarefa(indice):
    if 0 <= indice < len(tarefas):
        removida = tarefas.pop(indice)
        print(f"Tarefa '{removida['nome']}' removida.")
    else:
        print("Índice inválido.")