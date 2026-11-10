import pytest
from fila import Fila


def test_fila_vazia():
    fila = Fila()
    assert fila.aguardando == 0


def test_emitir_normal():
    fila = Fila()
    assert fila.emitir("normal") == "N1"


def test_emitir_prioritaria():
    fila = Fila()
    assert fila.emitir("prioritaria") == "P1"
