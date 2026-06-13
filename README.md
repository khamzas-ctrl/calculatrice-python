# Calculatrice Python

Une calculatrice simple en Python avec les quatre opérations de base.

## Fonctions disponibles

- `additionner(a, b)` — retourne `a + b`
- `soustraire(a, b)` — retourne `a - b`
- `multiplier(a, b)` — retourne `a * b`
- `diviser(a, b)` — retourne `a / b` (lève `ValueError` si `b == 0`)

## Utilisation

```python
from calculatrice import additionner, diviser

print(additionner(3, 5))   # 8
print(diviser(10, 4))      # 2.5
```

## Tests

```bash
pytest tests/
```
