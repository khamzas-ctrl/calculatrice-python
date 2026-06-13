"""Orchestrateur : charge les données, calcule les ratios, exporte."""
import json
from pathlib import Path
from dataclasses import asdict

from reporting.ratios import calculer_tous_ratios
from reporting.exporters.csv_export import sauvegarder_csv
from reporting.exporters.json_export import sauvegarder_json
from reporting.exporters.excel_export import sauvegarder_excel
from reporting.exporters.pdf_export import sauvegarder_pdf


def charger_donnees(chemin: str) -> dict:
    with open(chemin, encoding="utf-8") as f:
        return json.load(f)


def construire_rapport(donnees: dict) -> dict:
    resultats = calculer_tous_ratios(donnees)
    return {
        "banque": donnees["banque"],
        "periode": donnees["periode"],
        "date_rapport": donnees["date_rapport"],
        "ratios": [asdict(r) for r in resultats],
        "conformite_globale": all(r.conforme for r in resultats),
    }


def generer_rapports(chemin_donnees: str, dossier_sortie: str = "output") -> dict:
    Path(dossier_sortie).mkdir(exist_ok=True)
    donnees = charger_donnees(chemin_donnees)
    rapport = construire_rapport(donnees)

    base = Path(dossier_sortie) / f"rapport_{donnees['periode']}"
    sauvegarder_csv(rapport, f"{base}.csv")
    sauvegarder_json(rapport, f"{base}.json")
    sauvegarder_excel(rapport, f"{base}.xlsx")
    sauvegarder_pdf(rapport, f"{base}.pdf")

    return rapport
