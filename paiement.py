
from math import ceil


def calculer_frais(montant, boursier=False):
    if montant < 500:
        raise ValueError("Minimum : 500 FCFA")

    if montant > 500000:
        raise ValueError("Maximum : 500 000 FCFA")

    if boursier:
        return 0

    if montant <= 10000:
        return 0

    return ceil(montant * 0.01)


def calculer_total(montant, boursier=False):
    frais = calculer_frais(montant, boursier)
    return montant + frais