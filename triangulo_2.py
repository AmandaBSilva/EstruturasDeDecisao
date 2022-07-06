from numpy import arccos
from math import degrees

a = float(input("Insira a primeira medida: "))
b = float(input("Insira a segunda medida: "))
c = float(input("Insira a terceira medida: "))

medidas = {a, b, c}

# Regra dos cossenos:
# a² = b² + c² - 2*b*c*cos(α)
# b² = a² + c² - 2*a*c*cos(β)
# c² = a² + b² - 2*a*b*cos(θ)

cossenos = [
    (a**2 - b**2 - c**2)/(-2*b*c),  # (a² - b² - c²)/(-2*b*c) = cos(α)
    (b**2 - a**2 - c**2)/(-2*a*c),  # (b² - a² - c²)/(-2*a*c) = cos(β)
    (c**2 - a**2 - b**2)/(-2*a*b)  # (c² - a² - b²)/(-2*a*b) = cos(θ)
]

angulos = [degrees(x) for x in arccos(cossenos)]

if 90 in angulos:
    print("Triângulo retângulo")

if len(medidas) == 2:
    print("Isósceles")
elif len(medidas) == 1:
    print("Equilátero")
else:
    print("Escaleno")
