#Retorna a posição onde o texto foi encontrado ou -1 se não encontrar.
# .find() - Busca silenciosa
texto = "Python é incrível"

print(texto.find("Python"))   # Saída: 0
print(texto.find("é"))        # Saída: 7
print(texto.find("Java"))     # Saída: -1 (não encontrou)