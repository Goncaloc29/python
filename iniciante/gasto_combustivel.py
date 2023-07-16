tempo_viagem = int(input(""))

velocidade = int(input(""))

distancia = tempo_viagem * velocidade

# Gasto de combustivel
media = 12

litros = distancia / media

print("%.3f" % litros)