'''Crie um programa que:

Verifica se a mensagem contém a palavra "prazo"

Substitui "LearnNow" por "EduTech"

Exibe a mensagem corrigida'''

# Dados
aviso_1 = "LearnNow informa: seu prazo de entrega vence em 3 dias."
aviso_2 = "LearnNow informa: atividade enviada com sucesso."
aviso_3 = "Atenção: o prazo foi encerrado. Contate o suporte LearnNow."

# Solução completa
mensagens = [aviso_1, aviso_2, aviso_3]

for mensagem in mensagens:
    # Verifica se tem "prazo"
    if "prazo" in mensagem:
        print("[PEDAGÓGICO] ", end="")
    else:
        print("[GERAL] ", end="")
    
    # Substitui o nome
    mensagem_corrigida = mensagem.replace("LearnNow", "EduTech")
    print(mensagem_corrigida)