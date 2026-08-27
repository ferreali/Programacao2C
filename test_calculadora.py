import pytest

from calculadora import (
    calcular_desconto,
    calcular_acrescimo,
    calcular_juros_simples,
    calcular_juros_compostos,
    calcular_parcela
)


def test_calcular_desconto():
    assert calcular_desconto(1000, 10) == 900


def test_desconto_de_zero_porcento():
    assert calcular_desconto(500, 0) == 500


def test_calcular_acrescimo():
    assert calcular_acrescimo(1000, 10) == 1100


def test_calcular_juros_simples():
    assert calcular_juros_simples(1000, 2, 5) == 1100


def test_calcular_juros_compostos():
    assert calcular_juros_compostos(1000, 10, 2) == 1210


def test_calcular_parcela():
    assert calcular_parcela(1200, 4) == 300


def test_parcela_com_quantidade_zero():
    with pytest.raises(ValueError):
        calcular_parcela(1200, 0)


def test_valor_negativo():
    with pytest.raises(ValueError):
        calcular_desconto(-1000, 10)