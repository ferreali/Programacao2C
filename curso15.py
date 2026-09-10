#Parâmetros do .replace():
# 1. texto_antigo (obrigatório)
# 2. texto_novo (obrigatório)
# 3. quantidade (opcional) - quantas vezes substituir

texto = "aaa bbb aaa bbb"
print(texto.replace("a", "x"))          # xxx bbb xxx bbb (todas)
print(texto.replace("a", "x", 2))       # xxa bbb aaa bbb (só 2 vezes)