import json


def exporter_json(rapport: dict, indent: int = 2) -> str:
    return json.dumps(rapport, ensure_ascii=False, indent=indent)


def sauvegarder_json(rapport: dict, chemin: str) -> None:
    with open(chemin, "w", encoding="utf-8") as f:
        f.write(exporter_json(rapport))
