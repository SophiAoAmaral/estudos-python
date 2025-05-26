imc = float(input("Digite seu imc: "))
if imc <18.6 : print("Abaixo do peso")
elif imc >=18.6 and imc<=24.9:
    print("Peso Ideal") 
elif imc >=25 and imc <=29.9:
    print("Sobrepeso")
elif imc >=30 and imc<=34.9:
    print("Obesidade Grau |")
elif imc >=35 and imc <=39.9:
    print("Obesidade Grau || (severa)")
else:
    print("Obesidade Grau ||| (morbida)")