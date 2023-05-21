#nadanie zmiennych

LIMIT_JEDNEJ_PACZKI = 20
ilosc_wyslanych_paczek = 1
laczna_liczba_kilogramow = 0
suma_pustych_kilogramow = 0
produkt = 0
idx = 0
nadmiar = 0
paczka = 0
liczba_produktow = int(input('Ile produktów chcesz wysłać?: '))

# wlasciwa czesc programu

for idx in range(liczba_produktow):
    idx += 1
    produkt -= produkt
    produkt += int(input('Podaj wagę produktu: '))
    paczka += produkt
    if produkt < 1 or produkt > 10:
        break
    elif paczka <= LIMIT_JEDNEJ_PACZKI:
        laczna_liczba_kilogramow += produkt
        continue
    elif paczka > LIMIT_JEDNEJ_PACZKI:
        ilosc_wyslanych_paczek += 1
        laczna_liczba_kilogramow += produkt
        nadmiar = paczka - LIMIT_JEDNEJ_PACZKI
        suma_pustych_kilogramow += nadmiar
        nadmiar -= nadmiar
        paczka -= paczka
        print('Paczka się zapełniła')
if ilosc_wyslanych_paczek <= 1:
    suma_pustych_kilogramow = LIMIT_JEDNEJ_PACZKI - paczka

# wyswietlenie wynikow

if ilosc_wyslanych_paczek == 1:
    print(f'Wysłano : {ilosc_wyslanych_paczek} paczkę')
elif ilosc_wyslanych_paczek > 1 or ilosc_wyslanych_paczek < 4 :
    print(f'Wysłano : {ilosc_wyslanych_paczek} paczki')
else:
    print(print(f'Wysłano : {ilosc_wyslanych_paczek} paczek'))
print(f'Wysłano : {laczna_liczba_kilogramow} kg')
print(f'Suma pustych kilogramów : {suma_pustych_kilogramow}')





