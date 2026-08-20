# Define uma função reutilizável chamada calcular_desconto.
# Ela recebe o valor original do produto e a porcentagem de desconto.
def calcular_desconto(valor_original, percentual_desconto):

    # Calcula quanto será descontado do valor original.
    # Exemplo: 10% de R$ 200,00 resulta em R$ 20,00.
    valor_desconto = valor_original * percentual_desconto / 100

    # Subtrai o desconto do valor original para encontrar o preço final.
    valor_final = valor_original - valor_desconto

    # Devolve o valor final para a parte do programa que chamou a função.
    return valor_final


# Cria uma lista vazia para armazenar os dados dos produtos.
produtos = []

# Exibe o título do sistema.
print("=== CAIXA RÁPIDO ===")


# O range(1, 4) gera os números 1, 2 e 3.
# Portanto, o bloco será executado três vezes.
for numero in range(1, 4):

    # Exibe o número do produto que está sendo cadastrado.
    # \n pula uma linha antes do texto.
    print(f"\n--- Produto {numero} ---")

    # Solicita o nome do produto.
    nome = input("Nome do produto: ")

    # Solicita o valor original do produto.
    # replace(",", ".") permite digitar 100,50 ou 100.50.
    # float() transforma o texto digitado em um número decimal.
    valor_original = float(
        input("Valor original: R$ ").replace(",", ".")
    )

    # Solicita a porcentagem de desconto.
    # O valor também é convertido para o tipo float.
    percentual_desconto = float(
        input("Porcentagem de desconto: ").replace(",", ".")
    )

    # Chama a função calcular_desconto().
    # Os valores digitados são enviados como argumentos.
    valor_final = calcular_desconto(
        valor_original,
        percentual_desconto
    )

    # Adiciona uma nova lista dentro da lista produtos.
    # Cada produto terá quatro informações:
    # nome, valor original, desconto e valor final.
    produtos.append(
        [
            nome,
            valor_original,
            percentual_desconto,
            valor_final
        ]
    )


# Início da exibição do recibo.
# \n pula uma linha e "=" * 48 cria uma linha com 48 sinais de igual.
print("\n" + "=" * 48)

# Exibe o título do recibo.
print("              RECIBO – CAIXA RÁPIDO")

# Exibe outra linha com 48 sinais de igual.
print("=" * 48)


# Variável acumuladora que guardará a soma dos valores sem desconto.
total_original = 0

# Variável acumuladora que guardará a soma dos valores com desconto.
total_final = 0


# Percorre cada produto armazenado na lista produtos.
for produto in produtos:

    # Recupera o nome, que está na posição 0.
    nome = produto[0]

    # Recupera o valor original, que está na posição 1.
    valor_original = produto[1]

    # Recupera o percentual de desconto, que está na posição 2.
    percentual_desconto = produto[2]

    # Recupera o valor final, que está na posição 3.
    valor_final = produto[3]

    # Soma o valor original ao total sem descontos.
    # É equivalente a:
    # total_original = total_original + valor_original
    total_original += valor_original

    # Soma o valor final ao total da compra.
    # É equivalente a:
    # total_final = total_final + valor_final
    total_final += valor_final

    # Exibe o nome do produto.
    print(f"\nProduto: {nome}")

    # Exibe o valor original com duas casas decimais.
    print(f"Valor original: R$ {valor_original:.2f}")

    # Exibe o percentual de desconto com uma casa decimal.
    print(f"Desconto: {percentual_desconto:.1f}%")

    # Exibe o valor final com duas casas decimais.
    print(f"Valor final: R$ {valor_final:.2f}")


# Calcula quanto o cliente economizou.
# Subtrai o total pago do total original.
economia = total_original - total_final


# Exibe uma linha separadora formada por 48 hífens.
print("\n" + "-" * 48)

# Exibe o total dos produtos antes dos descontos.
print(f"Total sem descontos: R$ {total_original:.2f}")

# Exibe o valor total economizado.
print(f"Economia obtida:     R$ {economia:.2f}")

# Exibe o valor que o cliente deverá pagar.
print(f"TOTAL DA COMPRA:     R$ {total_final:.2f}")

# Finaliza o recibo com uma linha formada por sinais de igual.
print("=" * 48)
