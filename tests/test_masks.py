import pytest

from src.masks import number_account, number_card


@pytest.fixture
def my_card() -> str:
    return "7000792289606361"


def test_number_card(my_card: str) -> None:
    assert number_card(my_card) == "7000 79** **** 6361"


@pytest.fixture
def my_account() -> str:
    return "73654108430135874305"


def test_number_account(my_account: str) -> None:
    assert number_account(my_account) == "**4305"
