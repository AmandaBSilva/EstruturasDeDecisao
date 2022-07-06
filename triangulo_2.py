from numpy import arccos
from math import degrees

m1 = float(input("Insira a primeira medida: "))
m2 = float(input("Insira a segunda medida: "))
m3 = float(input("Insira a terceira medida: "))

medidas = {m1, m2, m3}

cossenos = [
    (m1**2 - m2**2 - m3**2)/(-2*m2*m3),
    (m2**2 - m1**2 - m3**2)/(-2*m1*m3),
    (m3**2 - m1**2 - m2**2)/(-2*m1*m2)
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
