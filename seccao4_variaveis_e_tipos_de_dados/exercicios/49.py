""" Faça um programa para leia o horário (hora, minuto e segundo) de inicio e a duração, em
segundos, de uma experiência biológica. O programa deve resultar com o novo horário
(hora, minuto e segundo) do termino da mesma. """


# receber os valores do utilizador
inicio = input("Digite o inicio da experiencia (hh:mm:ss): ") 

duracao = int(input("Introduza a duração em segundos do total da experiencia: "))

# separar os valores
valores_inicio = inicio.split(":")


# Atribuir os valores a variáveis
hora_inicio = int(valores_inicio[0])
minutos_inicio = int(valores_inicio[1])
segundos_inicio = int(valores_inicio[2])

# Converter o horario de inicio para segundos
segundos_inicio = hora_inicio * 3600 + minutos_inicio * 60 + segundos_inicio

# Somar os segundos de inicio com a duração
segundos_total = segundos_inicio + duracao

# Converter os segundos totais para horas, minutos e segundos

# divisao inteira // pelo numero de segundos que uma hora tem 3600
hora_termino = segundos_total // 3600
# precisamos de calcular primeiro o modulo do total de segundos por 3600 para termos os segundos não contabilizados nas horas
minuto_termino = (segundos_total % 3600) // 60
# precisamos de calcular o modulo do total de seguntos por 60 para termos os segundos que não foram contabilizados nos minutos porque fazemos sempre divisões inteiras //
segundo_termino = segundos_total % 60

# Imprimir horário de término da experiência biológica
print("O horário de término da experiência biológica é:", hora_termino,":",minuto_termino,":",segundo_termino)




