from tarefas import (
    adicionar_tarefa,
    listar_tarefas,
    marcar_concluida,
    remover_tarefa
)

while True:
    print("\n=== GERENCIADOR DE TAREFAS ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Marcar tarefa como concluída")
    print("4 - Remover tarefa")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome da tarefa: ")
        adicionar_tarefa(nome)

    elif opcao == "2":
        listar_tarefas()

    elif opcao == "3":
        listar_tarefas()
        try:
            indice = int(input("Número da tarefa concluída: ")) - 1
            marcar_concluida(indice)
        except ValueError:
            print("Digite um número válido.")

    elif opcao == "4":
        listar_tarefas()
        try:
            indice = int(input("Número da tarefa a remover: ")) - 1
            remover_tarefa(indice)
        except ValueError:
            print("Digite um número válido.")

    elif opcao == "5":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida!")