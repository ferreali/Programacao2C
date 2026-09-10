'''index() - Busca que gera erro
Retorna a posição ou lança um ValueError se não encontrar.'''
texto = "Python é incrível"

print(texto.index("Python"))  # Saída: 0
print(texto.index("Java"))    # ❌ ValueError: substring not found