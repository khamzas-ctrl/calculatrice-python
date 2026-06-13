# Reporting Réglementaire Bancaire (Bâle III)

Application Python de calcul et d'export des ratios prudentiels Bâle III.

## Ratios calculés

| Ratio | Seuil réglementaire | Description |
|---|---|---|
| **CAR** — Capital Adequacy Ratio | ≥ 8% | (Tier1 + Tier2) / RWA |
| **LCR** — Liquidity Coverage Ratio | ≥ 100% | HQLA / Sorties nettes 30j |
| **NSFR** — Net Stable Funding Ratio | ≥ 100% | ASF / RSF |
| **Ratio de levier** | ≥ 3% | Tier1 / Exposition totale |

## Installation

```bash
pip install -r requirements.txt
```

## Utilisation

```bash
python main.py data/exemple_banque.json
```

Les rapports sont générés dans le dossier `output/` :
- `rapport_T4-2025.csv`
- `rapport_T4-2025.json`
- `rapport_T4-2025.xlsx`
- `rapport_T4-2025.pdf`

## Format des données d'entrée

```json
{
  "banque": "Banque Exemple SA",
  "periode": "T4-2025",
  "date_rapport": "2025-12-31",
  "fonds_propres": { "tier1": 12500000, "tier2": 2500000 },
  "actifs_ponderes_risque": 95000000,
  "actifs_liquides_hqla": 18000000,
  "sorties_nettes_30j": 14000000,
  "financement_stable_disponible": 55000000,
  "financement_stable_requis": 48000000,
  "exposition_totale_levier": 210000000
}
```

## Tests

```bash
pytest tests/ -v
```
