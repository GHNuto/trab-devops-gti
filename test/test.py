import pytest
from src.main import *
from unittest.mock import patch
import asyncio


@pytest.fixture
def run_async_test():

    yield


def test_root(run_async_test):
    result = asyncio.run(read_root())
    assert result == {"ola": "mundo"}


def test_funcaoteste(run_async_test):
    with patch('src.main.random.randint', return_value=12345):
        result = asyncio.run(funcaoteste())
    assert result == {"teste": True, "num_aleatorio": 12345}


def test_jogar_dado(run_async_test):
    with patch('src.main.random.randint', return_value=4):
        result = asyncio.run(jogar_dado())
    assert result == {"resultado_dado": 4}


def test_saudacao_personalizada(run_async_test):
    result = asyncio.run(saudacao_personalizada("Gustavo"))
    assert result == {"mensagem": "Olá, Gustavo! Seja bem-vindo à API."}


def test_checar_status(run_async_test):
    result = asyncio.run(checar_status())
    assert result == {"status": "online", "servidor": "funcionando perfeitamente"}