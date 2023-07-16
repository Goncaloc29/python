from itertools import product

# 'abc'
symbols = set(input('insira os símbolos da linguagem ("01", "abc", etc.): '))

# ['1', '2', '3']
combinations = \
    list(input('insira as combinações desejadas (0,1,2,3...): ').split(','))

# ['1', '2', '3'] -> [1, 2, 3]
combinations = list(map(lambda x: int(x), combinations))

for i in combinations:
    strings = list(map(lambda x: ''.join(tuple(x)),
                       set(product(symbols, repeat=i))))
    strings.sort()
    for s in strings:
        print(s)
