'''Parsing Completo com Estrutura
Crie um dicionário para cada log processado:'''

def parse_log(log):
    """Converte uma linha de log em um dicionário estruturado"""
    campos = log.split(" | ")
    
    # Extraindo dados
    timestamp = campos[0]
    severidade = campos[1]
    modulo = campos[2].replace("Módulo: ", "")
    ip = campos[3].replace("IP: ", "")
    mensagem = campos[4]
    
    return {
        "timestamp": timestamp,
        "severidade": severidade,
        "modulo": modulo,
        "ip": ip,
        "mensagem": mensagem
    }

# Testando
log = "2026-09-03 | ERRO | Módulo: Login | IP: 192.168.1.1 | Usuário não encontrado"
dados = parse_log(log)

print("DADOS ESTRUTURADOS:")
for chave, valor in dados.items():
    print(f"  {chave}: {valor}")