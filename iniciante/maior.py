entrada1 = input()

str = entrada1.split(" ")

a = int(str[0])
b = int(str[1])
c = int(str[2])

if a > b and a > c:
    print("%deh o maior" % a)

if b > a and b > c:
    print("%deh o maior" % b)

if c > a and c > b:
    print("%d eh o maior" % c)

