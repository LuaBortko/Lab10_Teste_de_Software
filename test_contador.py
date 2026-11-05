import pytest
from contador import contar_palavras


def test_contar_teste():
    a = "teste"
    assert contar_palavras(a) == {"teste": 1}


def test_contar_vazio():
    a = ""
    assert contar_palavras(a) == {}
