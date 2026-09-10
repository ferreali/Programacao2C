'''Strings são IMUTÁVEIS = Não podem ser modificadas depois de criadas'''
nome = "João"
# nome[0] = "J"  #ERRO! TypeError: 'str' object does not support item assignment

# A forma correta é CRIAR UMA NOVA STRING
nome_corrigido = "J" + nome[1:]  # Cria nova string
print(nome_corrigido)  # Saída: João