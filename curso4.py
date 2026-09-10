'''.split() para separar os campos por um caractere, .find() para procurar palavras-chave e 
slicing para pegar partes específicas!”'''
log = "2026-09-03 | ERRO | Módulo: Login | IP: 192.168.1.1"
campos = log.split(" | ")
if campos[1] == "ERRO":
    print("Alerta! Um erro foi encontrado!")