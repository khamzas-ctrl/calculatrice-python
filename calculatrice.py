def additionner(a, b):
    return a + b


def soustraire(a, b):
    return a - b


def multiplier(a, b):
    return a * b


def diviser(a, b):
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b
