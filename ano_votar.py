ano_atual = int(input("Qual é o ano atual? "))
ano_nascimeto = int(input("Qual é o ano em que você nasceu? "))

if (ano_atual - ano_nascimeto) >= 16:
    print("Você poderá votar esse ano.")
else:
    print("Você não poderá votar esse ano.")
