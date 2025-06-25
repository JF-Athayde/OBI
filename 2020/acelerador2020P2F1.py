km_totais = int(input())

if km_totais == 6:
    print(1)
elif km_totais == 7:
    print(2)
elif km_totais == 8:
    print(3)

elif km_totais > 8:
    numero_de_voltas = int((km_totais-5)/8)
    voltas_km = numero_de_voltas*8
    
    r = km_totais-voltas_km

    if r == 6:
        print(1)
    elif r == 7:
        print(2)
    elif r == 8:
        print(3)