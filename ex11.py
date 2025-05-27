#determinacao da situacao em funcao da pressao arterial

sist = int(input("Sistolica: "))
diast = int(input("Diastolica: "))
if sist < 120 and diast <80 :
    print("Normal")
elif diast < 80 and sist <130 and sist >=120:
    print("Elevada")

