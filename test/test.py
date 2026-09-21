from src.main import *
from unittest.mock import patch


def test_root():
    import asyncio
    result = asyncio.run(read_root())
    yield
    assert result == {"ola": "mundo"}


def test_funcaoteste():
    import asyncio
    with patch('src.main.random.randint', return_value=12345):
        result = asyncio.run(funcaoteste())
        yield
    assert result == {"teste": True, "num_aleatorio": 12345}


def test_jogar_dado():
    import asyncio
    with patch('src.main.random.randint', return_value=4):
        result = asyncio.run(jogar_dado())
        yield
    assert result == {"resultado_dado": 4}


def test_saudacao_personalizada():
    import asyncio
    result = asyncio.run(saudacao_personalizada("Gustavo"))
    yield
    assert result == {"mensagem": "Olá, Gustavo! Seja bem-vindo à API."}


def test_checar_status():
    import asyncio
    result = asyncio.run(checar_status())
    yield
    assert result == {"status": "online", "servidor": "funcionando perfeitamente"}