""" Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de
sua idade e do ano atual. """
import _datetime

idade = int(input("Qual a sua idade: "))

ano_nascimento = 2023 - idade

ano_atual = _datetime.datetime.now().year

ano_nascimento = ano_atual - idade

print("Você nasceu em",ano_nascimento)