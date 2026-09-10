#Substitui um trecho por outro e retorna uma nova string.
mensagem = "LearnNow informa: seu prazo vence hoje."

# Substituir "LearnNow" por "EduTech"
nova_mensagem = mensagem.replace("LearnNow", "EduTech")
print(nova_mensagem)  # EduTech informa: seu prazo vence hoje.

# A string original NÃO foi alterada!
print(mensagem)  # LearnNow informa: seu prazo vence hoje.