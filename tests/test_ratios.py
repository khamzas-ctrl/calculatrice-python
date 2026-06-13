import pytest
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from reporting.ratios import calculer_car, calculer_lcr, calculer_nsfr, calculer_levier, calculer_tous_ratios


DONNEES_TEST = {
    "banque": "Banque Test",
    "periode": "T1-2025",
    "date_rapport": "2025-03-31",
    "fonds_propres": {"tier1": 12_500_000, "tier2": 2_500_000},
    "actifs_ponderes_risque": 95_000_000,
    "actifs_liquides_hqla": 18_000_000,
    "sorties_nettes_30j": 14_000_000,
    "financement_stable_disponible": 55_000_000,
    "financement_stable_requis": 48_000_000,
    "exposition_totale_levier": 210_000_000,
}


class TestCAR:
    def test_valeur(self):
        r = calculer_car(12_500_000, 2_500_000, 95_000_000)
        assert abs(r.valeur - 15_000_000 / 95_000_000) < 1e-10

    def test_conforme_au_dessus_seuil(self):
        r = calculer_car(8_000_000, 0, 100_000_000)  # exactement 8%
        assert r.conforme is True

    def test_non_conforme_en_dessous_seuil(self):
        r = calculer_car(5_000_000, 0, 100_000_000)  # 5% < 8%
        assert r.conforme is False

    def test_rwa_zero_leve_erreur(self):
        with pytest.raises(ValueError):
            calculer_car(1_000_000, 0, 0)


class TestLCR:
    def test_valeur(self):
        r = calculer_lcr(18_000_000, 14_000_000)
        assert abs(r.valeur - 18 / 14) < 1e-10

    def test_conforme(self):
        assert calculer_lcr(15_000_000, 14_000_000).conforme is True

    def test_non_conforme(self):
        assert calculer_lcr(10_000_000, 14_000_000).conforme is False

    def test_sorties_zero_leve_erreur(self):
        with pytest.raises(ValueError):
            calculer_lcr(1_000_000, 0)


class TestNSFR:
    def test_conforme(self):
        assert calculer_nsfr(55_000_000, 48_000_000).conforme is True

    def test_non_conforme(self):
        assert calculer_nsfr(40_000_000, 48_000_000).conforme is False


class TestLevier:
    def test_conforme(self):
        assert calculer_levier(12_500_000, 210_000_000).conforme is True

    def test_non_conforme(self):
        assert calculer_levier(1_000_000, 210_000_000).conforme is False


def test_calculer_tous_ratios_retourne_quatre_ratios():
    ratios = calculer_tous_ratios(DONNEES_TEST)
    assert len(ratios) == 4


def test_tous_ratios_conformes_avec_donnees_exemple():
    ratios = calculer_tous_ratios(DONNEES_TEST)
    assert all(r.conforme for r in ratios)
