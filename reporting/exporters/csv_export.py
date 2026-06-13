import csv
import io


def exporter_csv(rapport: dict) -> str:
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Banque", rapport["banque"]])
    writer.writerow(["Période", rapport["periode"]])
    writer.writerow(["Date", rapport["date_rapport"]])
    writer.writerow([])
    writer.writerow(["Ratio", "Valeur (%)", "Seuil (%)", "Conforme"])
    for r in rapport["ratios"]:
        writer.writerow([
            r["nom"],
            f"{r['valeur'] * 100:.2f}",
            f"{r['seuil'] * 100:.2f}",
            "OUI" if r["conforme"] else "NON",
        ])
    return output.getvalue()


def sauvegarder_csv(rapport: dict, chemin: str) -> None:
    with open(chemin, "w", newline="", encoding="utf-8") as f:
        f.write(exporter_csv(rapport))
