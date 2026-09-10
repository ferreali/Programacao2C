'''Slicing (Fatiamento)
Técnica para extrair um trecho específico de uma string.'''
#Sintaxe: [inicio:fim:passo]
'''Parâmetro	Descrição
inicio	        Índice onde começa (incluído)
fim	            Índice onde termina (NÃO incluído)
passo	        Intervalo entre caracteres (opcional)'''

texto = "RELATORIO-2024-01"
# Índices: 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
#          R  E  L  A  T  O  R  I  O  -  2  0  2  4  -  0  1

# Extraindo o ano
ano = texto[9:13]  # Do índice 9 até o 12 (13 não é incluído)
print(ano)  # 2024

# Extraindo o mês
mes = texto[14:]  # Do índice 14 até o final
print(mes)  # 01

# Extraindo o nome
nome = texto[:8]  # Do início até o índice 7
print(nome)  # RELATORIO
