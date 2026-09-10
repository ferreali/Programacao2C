#Um log é um registro cronológico de eventos gerado por sistemas. 
# Cada linha é uma string com campos separados por delimitadores.

#Dado o log abaixo, extraia todos os campos:

log = "2026-09-03 | ERRO | Módulo: Login | IP: 192.168.1.1 | Usuário não encontrado"

# Solução com split
campos = log.split(" | ")
timestamp = campos[0]
severidade = campos[1]
modulo = campos[2]
ip = campos[3]
mensagem = campos[4]

print(f"Data: {timestamp}")
print(f"Severidade: {severidade}")
print(f"Módulo: {modulo}")
print(f"IP: {ip}")
print(f"Mensagem: {mensagem}")