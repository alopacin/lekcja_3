#nadanie zmiennych

LIMIT_JEDNEJ_PACZKI = 20
ilosc_wyslanych_paczek = 1
laczna_liczba_kilogramow = 0
suma_pustych_kilogramow = 0
produkt = 0
idx = []
nadmiar = 0
paczka = 0
# wlasciwa czesc programu

liczba_produktow = int(input('Ile produktów chcesz wysłać?: '))
for _ in range(liczba_produktow):
    produkt = int(input('Podaj wagę produktu: '))
    paczka += produkt
    if produkt < 1 or produkt > 10:
        break
    elif paczka <= LIMIT_JEDNEJ_PACZKI:
        laczna_liczba_kilogramow += produkt
        produkt = 0
        continue
    elif paczka == LIMIT_JEDNEJ_PACZKI :
        laczna_liczba_kilogramow += produkt
        ilosc_wyslanych_paczek += 1
        paczka = 0
        produkt = 0
        continue
    elif paczka > LIMIT_JEDNEJ_PACZKI:
        paczka -= produkt
        nadmiar = LIMIT_JEDNEJ_PACZKI - paczka
        suma_pustych_kilogramow += nadmiar
        laczna_liczba_kilogramow += paczka
        paczka += produkt
        nadmiar = 0
        paczka = 0
        produkt = 0
        ilosc_wyslanych_paczek += 1
        continue
if ilosc_wyslanych_paczek <= 1 :
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






