"""Operações básicas de uma calculadora financeira."""


def validar_valor(valor):
    """Verifica se o valor financeiro não é negativo."""
    if valor < 0:
        raise ValueError("O valor não pode ser negativo.")


def calcular_desconto(valor, percentual):
    """Retorna o valor final depois da aplicação do desconto."""
    validar_valor(valor)
    validar_valor(percentual)

    resultado = valor * (1 - percentual / 100)
    return round(resultado, 2)


def calcular_acrescimo(valor, percentual):
    """Retorna o valor final depois da aplicação do acréscimo."""
    validar_valor(valor)
    validar_valor(percentual)

    resultado = valor * (1 + percentual / 100)
    return round(resultado, 2)


def calcular_juros_simples(capital, taxa, periodo):
    """Calcula o montante utilizando juros simples."""
    validar_valor(capital)
    validar_valor(taxa)
    validar_valor(periodo)

    montante = capital * (1 + taxa / 100 * periodo)
    return round(montante, 2)


def calcular_juros_compostos(capital, taxa, periodo):
    """Calcula o montante utilizando juros compostos."""
    validar_valor(capital)
    validar_valor(taxa)
    validar_valor(periodo)

    montante = capital * (1 + taxa / 100) ** periodo
    return round(montante, 2)


def calcular_parcela(valor_total, quantidade):
    """Divide um valor em parcelas iguais."""
    validar_valor(valor_total)

    if quantidade <= 0:
        raise ValueError(
            "A quantidade de parcelas deve ser maior que zero."
        )

    return round(valor_total / quantidade, 2)