#Operador in - Verificação booleana
#Verifica se um texto existe dentro de outro (retorna True ou False).
texto = "Python é incrível"

print("Python" in texto)   # True
print("Java" in texto)     # False

#É case-sensitive (diferencia maiúsculas de minúsculas)!'''
'''texto = "Erro no sistema"
print("erro" in texto)  # False (porque é "Erro" com E maiúsculo)

# Solução: padronizar com .lower() ou .upper()
texto_lower = texto.lower()
print("erro" in texto_lower)  # True'''