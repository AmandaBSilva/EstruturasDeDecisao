A = float(input("Insira a altura da pessoa A, em metros: "))
B = float(input("Insira a altura da pessoa B, em metros: "))

maior, menor = max(A, B), min(A, B)

if maior == menor:
    print("Ambos tem a mesma altura")
else:
    print(f"{maior} é maior que {menor}")
