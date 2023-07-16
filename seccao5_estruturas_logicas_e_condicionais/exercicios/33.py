"""
Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo, calcule e escreva o preço novo, e escreva uma mensagem em função do preço novo (de acordo com a segunda tabela).

"""

valores_antigos = {
    "intervalo1": {"minimo": 0, "maximo": 50, "aumento": 0.05},
    "intervalo2": {"minimo": 50, "maximo": 100, "aumento": 0.10}, 
    "intervalo3": {"minimo": 100, "maximo": None, "aumento": 0.15}
}

preco_antigo = float(input("Introduza o preço antigo: "))

# percorrer o dicionario a comparar preco_antigo com os valores minimo e maximo

if preco_antigo >= valores_antigos["intervalo1"]["minimo"] and preco_antigo <= valores_antigos["intervalo1"]["maximo"]:
    preco_novo = preco_antigo + preco_antigo * valores_antigos["intervalo1"]["aumento"]
    print("Preço novo: {:.2f}".format(preco_novo))
    if preco_novo <= 80:
        print("Barato")
    elif preco_novo > 80 and preco_novo <= 120:
        print("Normal")
    elif preco_novo > 120 and preco_novo <= 200:
        print("Caro")
    else:
        print("Muito caro")

if preco_antigo > valores_antigos["intervalo2"]["minimo"] and preco_antigo <= valores_antigos["intervalo2"]["maximo"]:
    preco_novo = preco_antigo + preco_antigo * valores_antigos["intervalo2"]["aumento"]
    print("Preço novo: {:.2f}".format(preco_novo))
    if preco_novo <= 80:
        print("Barato")
    elif preco_novo > 80 and preco_novo <= 120:
        print("Normal")
    elif preco_novo > 120 and preco_novo <= 200:
        print("Caro")
    else:
        print("Muito caro")

if preco_antigo > valores_antigos["intervalo3"]["minimo"] and preco_antigo <= valores_antigos["intervalo3"]["maximo"]:
    preco_novo = preco_antigo + preco_antigo * valores_antigos["intervalo3"]["aumento"]
    print("Preço novo: {:.2f}".format(preco_novo))
    if preco_novo <= 80:
        print("Barato")
    elif preco_novo > 80 and preco_novo <= 120:
        print("Normal")
    elif preco_novo > 120 and preco_novo <= 200:
        print("Caro")
    else:
        print("Muito caro")

