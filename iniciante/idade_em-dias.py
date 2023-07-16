dias = int(input(""))


resto = dias // 365
print("{} ano(s)".format(resto))
dias = dias % 365

resto = dias // 30
print("{} mes(es)".format(resto))
dias = dias % 30

print("{} dia(s)".format(dias))


