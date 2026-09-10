'''Exercício 2.3 - Localizando Posições
Use .find() para encontrar a posição de "LearnNow" em cada mensagem:'''

aviso_1 = "LearnNow informa: seu prazo de entrega vence em 3 dias."
aviso_2 = "LearnNow informa: atividade enviada com sucesso."
aviso_3 = "Atenção: o prazo foi encerrado. Contate o suporte LearnNow."

print(aviso_1.find("LearnNow"))  # 0
print(aviso_2.find("LearnNow"))  # 0
print(aviso_3.find("LearnNow"))  # 48 (posição onde começa)