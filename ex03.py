numero = int(input("informe o valor inteiro de 4 digitos: "))
if numero<1111 or numero>9999: print("Valor invalido, nao tem 4 digitos")
else:
    milhar = numero//1000
    resto = numero%1000
    centena = resto//100
    resto = resto%100
    dezena = resto//10
    unidade = resto%10
    invertido = unidade * 1000 + dezena * 100 + centena * 10 + milhar
    print("Valor ao contrario:", invertido)
if numero==invertido:print("Capcun")
else:print("Nao e Capcum")