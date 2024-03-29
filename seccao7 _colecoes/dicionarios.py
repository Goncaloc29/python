"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}

# Exemplos

# Forma 1 (Mais comum)

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

# Forma 2 (Menos comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')

print(paises)
print(type(paises))

# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla

print(paises['br'])
print(paises['py'])

# OBS: Caso tentemos fazer um acesso utilizando uma chave que não existe, teremos o erro KeyError

# Forma 2 - Acessando via get - Recomendada

print(paises.get('br'))
print(paises.get('ru'))

# Caso o get não encontre o objeto com a chave informada será retornado o valor None e não será gerado KeyError

pais = paises.get('ru')

if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o país')

# Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada

pais = paises.get('ru', 'Não encontrado')

print(f'Encontrei o país {pais}')

# Podemos verificar se determinada chave se encontra em um dicionário

print('br' in paises)
print('ru' in paises)

if 'ru' in paises:
    russia = paises['ru']

# Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla, dicionário, como chaves de dicionários

# Tuplas por exemplo são bastante interessantes de serem utilizadas como chaves de dicionários, pois as mesmas são imutáveis.

localidades = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7128, 74.0060): 'Escritório em Nova York',
    (37.7749, 122.4194): 'Escritório em São Paulo',
}

print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)

# Forma 1 - Mais comum  -  Acessando a chave e atribuindo um valor

receita['abr'] = 350

print(receita)

# Forma 2 - Menos comum - Utilizando o método update

novo_dado = {'mai': 500}

receita.update(novo_dado)  # receita.update({'mai': 500})

print(receita)

# Atualizando dados em um dicionário

# Forma 1

receita['mai'] = 550    # receita['mai'] = receita['mai'] + 100

print(receita)

# Forma 2

receita.update({'mai': 600})

print(receita)

# CONCLUSÃO 1: A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma.
# CONCLUSÃO 2: Em dicionários, NÃO podemos ter chaves repetidas.

# Remover dados de um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)

# Forma 1 - Mais comum

ret = receita.pop('mar')
print(ret)

print(receita)

# OBS 1: Aqui precisamos SEMPRE informar a chave, e caso não encontre o elemento, um KeyError é retornado.
# OBS 2: Ao removermos um objeto, o valor deste objeto é sempre retornado.

# Forma 2

del receita['fev']

print(receita)

# Se a chave não existir será gerado um KeyError
# Neste caso o valor removido não é retornado.

# Imagine que você tem um comércio eletrônico, onde temos um carrinho de compras na qual adicionamos produtos.

Carrinho de compras:

Produto 1:
Produto 2:
Produto 3:

# 1 - Poderíamos utilizar uma lista para isso? Sim!
# 2 - Poderíamos utilizar uma tupla para isso? Sim!
# 3 - Poderíamos utilizar um dicionário para isso? Sim!

Carrinho de compras:

Produto 1:
Produto 2:
Produto 3:

# Métodos de dicionários

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# Limpar o dicionário (Zerar dados)

d.clear()

print(d)

# Copiando um dicionário para outro

# Forma 1 - Deep Copy

novo = d.copy()

print(novo)
novo['d'] = 4

print(d)
print(novo)

# Forma 2 - Shallow Copy

novo = d

print(novo)
novo['d'] = 4

print(d)
print(novo)

# Veja que nos casos acima, copiamos os dados de d para novo. Mas e se d mudar? O novo também muda?

# Deep Copy: copia independente, ou seja, modificando um não afeta o outro. (novo = d.copy())
# Shallow Copy: copia dependente, ou seja, modificando um afeta o outro. (novo = d)

# Forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')

print(usuario)
print(type(usuario))

# O método fromkeys recebe dois parâmetros: um iterável e um valor.
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado.

veja = {}.fromkeys('teste', 'valor')

print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')

print(veja)

# O método fromkeys recebe dois parâmetros: um iterável e um valor.
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado.

# Exemplo mais complexo

usuario = {
    'nome': 'Gustavo',
    'pontos': 46
}

print(usuario)

# Imagine que você tem um comércio eletrônico, onde temos um carrinho de compras na qual adicionamos produtos.

Carrinho de compras:

Produto 1:
Produto 2:
Produto 3:

# 1 - Poderíamos utilizar uma lista para isso? Sim!
# 2 - Poderíamos utilizar uma tupla para isso? Sim!
# 3 - Poderíamos utilizar um dicionário para isso? Sim!

Carrinho de compras:

Produto 1:
Produto 2:
Produto 3:

# Métodos de dicionários

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# Limpar o dicionário (Zerar dados)

d.clear()

print(d)

# Copiando um dicionário para outro

# Forma 1 - Deep Copy

novo = d.copy()

print(novo)
novo['d'] = 4

print(d)
print(novo)

# Forma 2 - Shallow Copy

novo = d

print(novo)
novo['d'] = 4

print(d)
print(novo)

# Veja que nos casos acima, copiamos os dados de d para novo. Mas e se d mudar? O novo também muda?

# Deep Copy: copia independente, ou seja, modificando um não afeta o outro. (novo = d.copy())
# Shallow Copy: copia dependente, ou seja, modificando um afeta o outro. (novo = d)

# Forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')

print(usuario)
print(type(usuario))

# O método fromkeys recebe dois parâmetros: um iterável e um valor.
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado.

veja = {}.fromkeys('teste', 'valor')

print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')

print(veja)

# O método fromkeys recebe dois parâmetros: um iterável e um valor.
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado.

# Exemplo mais complexo

usuario = {
    'nome': 'Gustavo',
    'pontos': 46
}

print(usuario)

# Imagine que você tem um comércio eletrônico, onde temos um carrinho de compras na qual adicionamos produtos.

Carrinho de compras:

Produto 1:
Produto 2:
Produto 3:

# 1 - Poderíamos utilizar uma lista para isso? Sim!
# 2 - Poderíamos utilizar uma tupla para isso? Sim!
# 3 - Poderíamos utilizar um dicionário para isso? Sim
"""