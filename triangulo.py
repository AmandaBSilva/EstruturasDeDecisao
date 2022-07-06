m1 = float(input("Insira a primeira medida: "))
m2 = float(input("Insira a segunda medida: "))
m3 = float(input("Insira a terceira medida: "))

medidas = {m1, m2, m3}

if len(medidas) == 2:
    print("Isósceles")
elif len(medidas) == 1:
    print("Equilátero")
else:
    print("Escaleno")
