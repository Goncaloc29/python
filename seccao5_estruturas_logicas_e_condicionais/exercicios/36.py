""" Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser
paga ao vendedor. Para calcular a comissão, considere a tabela abaixo: """

venda = float(input("Introduza o valor da venda: "))

comissao = 0.0

if venda >= 100000:
    comissao = 700.00 + venda * 0.16
    print("Valor da comissão é: {:.2f} euros".format(comissao))
if venda < 100000 and venda >= 80000:
    comissao = 650.00 + venda * 0.14
    print("Valor da comissão é: {:.2f} euros".format(comissao))
if venda < 80000 and venda >= 60000:
    comissao = 600.00 + venda * 0.14
    print("Valor da comissão é: {:.2f} euros".format(comissao))
if venda < 60000 and venda >= 40000:
    comissao = 550.00 + venda * 0.14
    print("Valor da comissão é: {:.2f} euros".format(comissao))
if venda < 40000 and venda >= 20000:
    comissao = 500.00 + venda * 0.14
    print("Valor da comissão é: {:.2f} euros".format(comissao))
if venda < 20000:
    comissao = 400.00 + venda * 0.14
    print("Valor da comissão é: {:.2f} euros".format(comissao))