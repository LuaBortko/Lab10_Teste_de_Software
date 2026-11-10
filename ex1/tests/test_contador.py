import pytest
from contador import contar_palavras


def test_contar_teste():
    a = "teste"
    assert contar_palavras(a) == {"teste": 1}


def test_contar_vazio():
    a = ""
    assert contar_palavras(a) == {}


def test_contar_bom_dia():
    a = "bom dia"
    assert contar_palavras(a) == {"bom": 1, "dia": 1}


def test_contar_ignorar_pontos():
    a = "... !"
    assert contar_palavras(a) == {}


def test_contar_bom_dia_quebra_linha():
    a = "bom\ndia"
    assert contar_palavras(a) == {"bom": 1, "dia": 1}


def test_contar_mesma_palavra():
    a = "dia a dia"
    assert contar_palavras(a) == {"dia": 2, "a": 1}


def test_contar_dia_dia_com_pontuacao():
    a = ",dia, ;dia;"
    assert contar_palavras(a) == {"dia": 2}


def test_contar_dia_dia_com_pontuacao2():
    a = ":dia: ?dia?"
    assert contar_palavras(a) == {"dia": 2}


def test_contar_dia_dia_com_letra_maiuscula_minuscula():
    a = "Dia dia DIA"
    assert contar_palavras(a) == {"dia": 3}


def test_pontuacao_e_maiusculas():
    assert contar_palavras("fim. Fim!") == {"fim": 2}


def test_palavra_com_hifen():
    assert contar_palavras("guarda-chuva") == {"guarda-chuva": 1}
