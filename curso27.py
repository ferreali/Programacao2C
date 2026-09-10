#Filtrando Logs Críticos
#Separe os logs por severidade:

logs = [
    "2026-09-03 | INFO | Módulo: Auth | Usuário logado com sucesso",
    "2026-09-03 | ERRO | Módulo: Database | Falha na conexão",
    "2026-09-03 | WARNING | Módulo: Cache | Memória quase cheia",
    "2026-09-03 | ERRO | Módulo: Login | Senha incorreta para usuário admin"
]

# Separar por severidade
erros = []
avisos = []
informacoes = []

for log in logs:
    if "ERRO" in log:
        erros.append(log)
    elif "WARNING" in log:
        avisos.append(log)
    else:
        informacoes.append(log)

print(f"ERROS ({len(erros)}):")
for erro in erros:
    print(f"  - {erro}")

print(f"\nAVISOS ({len(avisos)}):")
for aviso in avisos:
    print(f"  - {aviso}")

print(f"\nINFORMAÇÕES ({len(informacoes)}):")
for info in informacoes:
    print(f"  - {info}")