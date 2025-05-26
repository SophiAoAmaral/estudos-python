horainicial = int(input("Informe a hora inicial do jogo: "))
minutoinicial = int(input("Informe o minuto inicial do jogo: "))
horafinal = int(input("Informe a hora final do jogo: "))
minutofinal = int(input("Informe o minuto final do jogo: "))

horarioinicial = horainicial *60 + minutoinicial
horariofinal = horafinal *60 + minutofinal

if horarioinicial < horariofinal : duracao = horariofinal-horarioinicial
else: duracao = 24*60 - horarioinicial + horariofinal

print("Horas: ", duracao//60)
print("Minutos", duracao%60)