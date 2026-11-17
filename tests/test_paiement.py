
import pytest

from paiement import calculer_frais, calculer_total


@pytest.mark.parametrize(
    "montant, frais_attendus",
    [
        (500, 0),
        (1000, 0),
        (10000, 0),
        (10001, 101),
        (20000, 200),
        (500000, 5000),
    ]
)
def test_calculer_frais(montant, frais_attendus):
    resultat = calculer_frais(montant)
    assert resultat == frais_attendus


@pytest.mark.parametrize(
    "montant",
    [
        499,
        0,
        -100,
        500001,
        600000,
    ]
)
def test_montants_invalides(montant):
    with pytest.raises(ValueError):
        calculer_frais(montant)


@pytest.mark.parametrize(
    "montant",
    [
        500,
        10000,
        10001,
        20000,
        500000,
    ]
)
def test_boursier_zero_frais(montant):
    resultat = calculer_frais(montant, boursier=True)
    assert resultat == 0


def test_calculer_total_sans_frais():
    resultat = calculer_total(10000)
    assert resultat == 10000


def test_calculer_total_avec_frais():
    resultat = calculer_total(20000)
    assert resultat == 20200


def test_calculer_total_boursier():
    resultat = calculer_total(20000, boursier=True)
    assert resultat == 20000


def test_arrondi_superieur():
    resultat = calculer_frais(10101)
    assert resultat == 102