"""Point d'entrée : génère tous les rapports depuis les données JSON."""
import sys
from reporting.rapport import generer_rapports


def afficher_resume(rapport: dict) -> None:
    statut = "CONFORME" if rapport["conformite_globale"] else "NON CONFORME"
    print(f"\n{'='*55}")
    print(f"  {rapport['banque']} - {rapport['periode']}")
    print(f"  Statut global : {statut}")
    print(f"{'='*55}")
    for r in rapport["ratios"]:
        icone = "OK" if r["conforme"] else "!!"
        print(f"  {icone}  {r['nom']:<35} {r['valeur']*100:6.2f}%  (seuil {r['seuil']*100:.0f}%)")
    print(f"{'='*55}\n")


if __name__ == "__main__":
    chemin = sys.argv[1] if len(sys.argv) > 1 else "data/exemple_banque.json"
    rapport = generer_rapports(chemin, dossier_sortie="output")
    afficher_resume(rapport)
    print("Rapports générés dans le dossier output/ (CSV, JSON, Excel, PDF)")
