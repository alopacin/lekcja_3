liczba_produktow = int(input('Ile produktów chcesz wysłać?: '))
LIMIT_JEDNEJ_PACZKI = 20
ilosc_wyslanych_paczek = 1
laczna_liczba_kilogramow = 0
suma_pustych_kilogramow = 0
waga_przedmiotu = 0
idx = 0
nadmiar = 0
jedna_paczka = 0

for idx in range(liczba_produktow):
    waga_przedmiotu += int(input('Podaj wagę przedmiotu: '))
    jedna_paczka += waga_przedmiotu
    if waga_przedmiotu < 1 or waga_przedmiotu > 10:
        break
    elif jedna_paczka < LIMIT_JEDNEJ_PACZKI:
        laczna_liczba_kilogramow += waga_przedmiotu
        waga_przedmiotu -= waga_przedmiotu
        continue
    elif jedna_paczka > LIMIT_JEDNEJ_PACZKI:
        ilosc_wyslanych_paczek += 1
        nadmiar += jedna_paczka - 20
        suma_pustych_kilogramow += nadmiar
        jedna_paczka -= jedna_paczka
        waga_przedmiotu -= waga_przedmiotu
        continue
    elif jedna_paczka == LIMIT_JEDNEJ_PACZKI:
        ilosc_wyslanych_paczek += 1
        laczna_liczba_kilogramow += waga_przedmiotu
        jedna_paczka -= jedna_paczka
        waga_przedmiotu -= waga_przedmiotu

if ilosc_wyslanych_paczek == 1:
    print(f'Wysłano : {ilosc_wyslanych_paczek} paczkę')
elif ilosc_wyslanych_paczek > 1 or ilosc_wyslanych_paczek < 4 :
    print(f'Wysłano : {ilosc_wyslanych_paczek} paczki')
else:
    print(print(f'Wysłano : {ilosc_wyslanych_paczek} paczek'))
print(f'Wysłano : {laczna_liczba_kilogramow} kg')
print(f'Suma pustych kilogramów : {suma_pustych_kilogramow}')





