numero = input("Syötä numero:")
suurin = numero
pienin = numero

while numero != "":
    if int(numero) >= int(suurin):
        suurin = numero
        numero = input("Syötä numero:")
    elif int(numero) <= int(pienin):
        pienin = numero
        numero = input("Syötä numero:")

print("Suurin numero oli:", suurin)
print("Pienin numero oli:", pienin)
