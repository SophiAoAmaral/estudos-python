print("Digite sua altura: ")
altura =float(input())
print("Qual seu genero,  digite 1 para feminino e 2 para masculino")
genero = int(input())

if genero==1: peso= 62.1 * altura - 44.7
if genero==2: peso =72.7 *altura - 58
if genero!=1 and genero!=2:
    print("GENERO INVALIDO LEIA NOVAMENTE")
    peso=0
print("Peso ideal", peso)
 