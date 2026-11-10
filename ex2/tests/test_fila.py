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


def test_duas_normais():
    fila = Fila()

    fila.emitir("normal")
    fila.emitir("normal")

    assert fila.chamar() == "N1"
    assert fila.chamar() == "N2"


def test_duas_prioritarias():
    fila = Fila()

    fila.emitir("prioritaria")
    fila.emitir("prioritaria")

    assert fila.chamar() == "P1"
    assert fila.chamar() == "P2"


def test_prioritaria_passa_na_frente():
    fila = Fila()

    fila.emitir("normal")
    fila.emitir("prioritaria")

    assert fila.chamar() == "P1"
    assert fila.chamar() == "N1"
