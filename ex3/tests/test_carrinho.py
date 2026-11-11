import pytest
from carrinho import Carrinho


def test_carrinho_vazio():
    carrinho = Carrinho()
    assert carrinho.total == 0


def test_adicionar_preco():
    carrinho = Carrinho()
    carrinho.adicionar(2500)

    assert carrinho.total == 2500


def test_adicionar_quantidade():
    carrinho = Carrinho()
    carrinho.adicionar(2500, quantidade=2)

    assert carrinho.total == 5000


def test_preco_zero_rejeitado():
    carrinho = Carrinho()

    with pytest.raises(ValueError):
        carrinho.adicionar(0)


def test_cupom_dez():
    carrinho = Carrinho()
    carrinho.adicionar(5000)
    carrinho.aplicar_cupom("DEZ")

    assert carrinho.total == 4500


def test_cupom_desconhecido():
    carrinho = Carrinho()

    with pytest.raises(ValueError):
        carrinho.aplicar_cupom("XYZ")


def test_adicionar_apos_cupom():
    carrinho = Carrinho()
    carrinho.adicionar(1000)
    carrinho.aplicar_cupom("DEZ")
    carrinho.adicionar(1000)

    assert carrinho.total == 1800


def test_quantidade_zero_rejeitada():
    carrinho = Carrinho()

    with pytest.raises(ValueError):
        carrinho.adicionar(1000, quantidade=0)


def test_quantidade_negativa_rejeitada():
    carrinho = Carrinho()

    with pytest.raises(ValueError):
        carrinho.adicionar(1000, quantidade=-1)


def test_quantidade_fracionaria_rejeitada():
    carrinho = Carrinho()

    with pytest.raises(ValueError):
        carrinho.adicionar(1000, quantidade=1.5)
