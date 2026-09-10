#Manipulando Nomes
#Dado um nome completo, extraia o primeiro e o último nome:
nome_completo = "Ana Carolina Silva Santos"

# Extrair primeiro nome
primeiro_nome = nome_completo[:nome_completo.find(" ")]
print(primeiro_nome)  # Ana

# Extrair último nome (usando índices negativos)
ultimo_nome = nome_completo.split()[-1]
print(ultimo_nome)  # Santos

# Solução com slicing e find
ultimo_espaco = nome_completo.rfind(" ")
ultimo_nome2 = nome_completo[ultimo_espaco + 1:]
print(ultimo_nome2)  # Santos