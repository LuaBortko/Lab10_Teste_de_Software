import pytest
from contador import contar_palavras


def test_cortar_teste():
    a = "teste"
    assert contar_palavras(a) == {"teste": 1}
