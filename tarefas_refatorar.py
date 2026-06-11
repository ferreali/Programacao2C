# Lista inicial para teste
tarefas = ["estudar", "treinar", "entregar trabalho"]


# Função sem retorno (procedimento)
# Exibe todas as tarefas da lista
def exibir_tarefas(lista_tarefas):
    for tarefa in lista_tarefas:
        print(tarefa)


# Função com retorno
# Retorna a quantidade de tarefas
def contar_tarefas(lista_tarefas):
    return len(lista_tarefas)


# Função com retorno
# Retorna a primeira tarefa ou informa que a lista está vazia
def obter_primeira_tarefa(lista_tarefas):
    if len(lista_tarefas) == 0:
        return "vazio"
    return lista_tarefas[0]


# Programa principal
print("Lista de tarefas:")
exibir_tarefas(tarefas)

print("Quantidade:", contar_tarefas(tarefas))

print("Primeira tarefa:", obter_primeira_tarefa(tarefas))


# Teste com lista vazia
print("\nTeste com lista vazia")

tarefas = []

print("Lista de tarefas:")
exibir_tarefas(tarefas)

print("Quantidade:", contar_tarefas(tarefas))

print("Primeira tarefa:", obter_primeira_tarefa(tarefas))
