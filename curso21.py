#F-Strings (Formatação)
#Inserem valores de variáveis diretamente no texto.
nome = "Letícia"
ano = 2024
nota = 8.5

# F-string básica
print(f"Aluna: {nome}, Ano: {ano}, Nota: {nota}")
# Saída: Aluna: Letícia, Ano: 2024, Nota: 8.5

# Formatando números
print(f"Nota: {nota:.2f}")     # 8.50 (2 casas decimais)
print(f"Nota: {nota:>10}")     # "       8.5" (alinhado à direita)
print(f"Nota: {nota:<10}")     # "8.5       " (alinhado à esquerda)
print(f"Nota: {nota:^10}")     # "   8.5    " (centralizado)