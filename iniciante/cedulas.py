valor = int(input(""))

if valor > 1000000 or valor < 0:
    print("Valor invalido")

cedulas = [100, 50, 20, 10, 5, 2, 1]

# cedula é os valores do array

for cedula in cedulas:  # enquanto houver cedula no array ele entra e faz o seguinte
    # quantidade de cedulas é o valor dividido pela cedula    
    qtd_cedulas = valor // cedula   # exemplo 576 // 100 = 5 porque o // é uma divisão inteira
    print("{} nota(s) de R$ {},00".format(qtd_cedulas, cedula))     # imprime a quantidade de cedulas e a cedula em questão   
    valor = valor % cedula  # calcula o resto do valor para entrar no proximo loop

