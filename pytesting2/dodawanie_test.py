import pytest


@pytest.mark.parametrize("licbza, suma", [(5, 8), (2, 4)])
def test_dodawania(licbza,suma):
    assert licbza + licbza == suma
