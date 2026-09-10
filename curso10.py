'''Crie um programa que corrija a string "python para iniciantes" 
para "Python para iniciantes":'''
# Solução 1: Usando concatenação
#Concatenar significa juntar dois ou mais textos (strings) em uma única sequência
curso = "python para iniciantes"
curso_corrigido = "P" + curso[1:]
print(curso_corrigido)  # Python para iniciantes

# Solução 2: Usando replace (veremos na Aula 2)
curso_corrigido2 = curso.replace("p", "P", 1)
print(curso_corrigido2)  # Python para iniciantes

'''nome = "Alini"
sobrenome = "Alexandre"

nome_completo = nome + " " + sobrenome

print(nome_completo)'''