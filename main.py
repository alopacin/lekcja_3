#nadanie zmiennych

LIMIT_JEDNEJ_PACZKI = 20
ilosc_wyslanych_paczek = 1
laczna_liczba_kilogramow = 0
suma_pustych_kilogramow = 0
waga_przedmiotu = 0
idx = 0
nadmiar = 0
paczka = 0
liczba_produktow = int(input('Ile produktów chcesz wysłać?: '))

# wlasciwa czesc programu

for idx in range(liczba_produktow):
    waga_przedmiotu -= waga_przedmiotu
    waga_przedmiotu += int(input('Podaj wagę przedmiotu: '))
    paczka += waga_przedmiotu
    if waga_przedmiotu < 1 or waga_przedmiotu > 10:
        break
    elif paczka <= LIMIT_JEDNEJ_PACZKI:
        laczna_liczba_kilogramow += waga_przedmiotu
        continue
    elif paczka > LIMIT_JEDNEJ_PACZKI:
        laczna_liczba_kilogramow += waga_przedmiotu
        ilosc_wyslanych_paczek += 1
        nadmiar += paczka - LIMIT_JEDNEJ_PACZKI
        suma_pustych_kilogramow += nadmiar
        paczka -= paczka
        continue
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





