from src.main import *
from unittest.mock import patch


def test_root():
    result = read_root()
    yield
    assert result == {"ola": "mundo"}


def test_funcaoteste():
    with patch('src.main.random.randint', return_value=12345):
        result = funcaoteste()
        yield
    assert result == {"teste": True, "num_aleatorio": 12345}


def test_jogar_dado():
    with patch('src.main.random.randint', return_value=4):
        result = jogar_dado()
        yield
    assert result == {"resultado_dado": 4}


def test_saudacao_personalizada():
    result = saudacao_personalizada("Gustavo")
    yield
    assert result == {"mensagem": "Olá, Gustavo! Seja bem-vindo à API."}


def test_checar_status():
    result = checar_status()
    yield
    assert result == {"status": "online", "servidor": "funcionando perfeitamente"}