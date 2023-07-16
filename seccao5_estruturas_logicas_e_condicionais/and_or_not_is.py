# para p and, ambos os valores precisam ser true

ativo = True
logado = True

if ativo and logado:
    print('Bem vindo usuário')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')


# para o or, basta um dos valores ser true

ativo = True
logado = False

if ativo or logado:
    print('Bem vindo usuário')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')

# para o not, o valor do bollean é invertido

ativo = True
logado = False

if not ativo:
    print('Voce precisa ativar sua conta. Por favor, cheque seu e-mail')
else:
    print('Bem vindo usuário')

# para o is

ativo = True
logado = False

if ativo is True:
    print('Bem vindo usuário')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
    
