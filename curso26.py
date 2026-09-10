#Limpeza de Dados com .strip()
#Remova os espaços extras dos campos:

log = "2026-09-03 | ERRO | Módulo: Login | IP: 192.168.1.1 | Usuário não encontrado"
campos = log.split(" | ")

# Limpando cada campo
campos_limpos = [campo.strip() for campo in campos]
print(campos_limpos)
# ['2026-09-03', 'ERRO', 'Módulo: Login', 'IP: 192.168.1.1', 'Usuário não encontrado']