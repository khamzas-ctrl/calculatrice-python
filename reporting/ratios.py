"""Calculs des ratios prudentiels Bâle III."""
from dataclasses import dataclass


SEUIL_CAR = 0.08        # 8% minimum Bâle III
SEUIL_LCR = 1.0         # 100%
SEUIL_NSFR = 1.0        # 100%
SEUIL_LEVIER = 0.03     # 3%


@dataclass
class ResultatRatio:
    nom: str
    valeur: float
    seuil: float
    conforme: bool
    detail: dict


def calculer_car(tier1: float, tier2: float, actifs_ponderes: float) -> ResultatRatio:
    """Capital Adequacy Ratio = (Tier1 + Tier2) / RWA."""
    if actifs_ponderes <= 0:
        raise ValueError("Les actifs pondérés doivent être positifs")
    valeur = (tier1 + tier2) / actifs_ponderes
    return ResultatRatio(
        nom="Capital Adequacy Ratio (CAR)",
        valeur=valeur,
        seuil=SEUIL_CAR,
        conforme=valeur >= SEUIL_CAR,
        detail={"tier1": tier1, "tier2": tier2, "rwa": actifs_ponderes},
    )


def calculer_lcr(hqla: float, sorties_nettes_30j: float) -> ResultatRatio:
    """Liquidity Coverage Ratio = HQLA / Sorties nettes sur 30 jours."""
    if sorties_nettes_30j <= 0:
        raise ValueError("Les sorties nettes doivent être positives")
    valeur = hqla / sorties_nettes_30j
    return ResultatRatio(
        nom="Liquidity Coverage Ratio (LCR)",
        valeur=valeur,
        seuil=SEUIL_LCR,
        conforme=valeur >= SEUIL_LCR,
        detail={"hqla": hqla, "sorties_nettes_30j": sorties_nettes_30j},
    )


def calculer_nsfr(financement_dispo: float, financement_requis: float) -> ResultatRatio:
    """Net Stable Funding Ratio = ASF / RSF."""
    if financement_requis <= 0:
        raise ValueError("Le financement requis doit être positif")
    valeur = financement_dispo / financement_requis
    return ResultatRatio(
        nom="Net Stable Funding Ratio (NSFR)",
        valeur=valeur,
        seuil=SEUIL_NSFR,
        conforme=valeur >= SEUIL_NSFR,
        detail={"asf": financement_dispo, "rsf": financement_requis},
    )


def calculer_levier(tier1: float, exposition_totale: float) -> ResultatRatio:
    """Ratio de levier = Tier1 / Exposition totale."""
    if exposition_totale <= 0:
        raise ValueError("L'exposition totale doit être positive")
    valeur = tier1 / exposition_totale
    return ResultatRatio(
        nom="Ratio de levier",
        valeur=valeur,
        seuil=SEUIL_LEVIER,
        conforme=valeur >= SEUIL_LEVIER,
        detail={"tier1": tier1, "exposition": exposition_totale},
    )


def calculer_tous_ratios(donnees: dict) -> list[ResultatRatio]:
    fp = donnees["fonds_propres"]
    return [
        calculer_car(fp["tier1"], fp["tier2"], donnees["actifs_ponderes_risque"]),
        calculer_lcr(donnees["actifs_liquides_hqla"], donnees["sorties_nettes_30j"]),
        calculer_nsfr(donnees["financement_stable_disponible"], donnees["financement_stable_requis"]),
        calculer_levier(fp["tier1"], donnees["exposition_totale_levier"]),
    ]
