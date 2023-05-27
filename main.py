#nadanie zmiennych

LIMIT_JEDNEJ_PACZKI = 20
ilosc_wyslanych_paczek = 1
laczna_liczba_kilogramow = 0
suma_pustych_kilogramow = 0
nadmiar = 0
paczka = 0

# wlasciwa czesc programu
liczba_produktow = int(input('Ile produktów chcesz wysłać?: '))
for _ in range(liczba_produktow):
    produkt = int(input('Podaj wagę produktu: '))
    paczka += produkt
    print(paczka)
    print(produkt)
    print(laczna_liczba_kilogramow)
    print(suma_pustych_kilogramow)
    if produkt < 1 or produkt > 10:
        break
    elif paczka < LIMIT_JEDNEJ_PACZKI:
        laczna_liczba_kilogramow += produkt
        produkt = 0
        print('Dodano produkt do paczki')
    elif paczka == LIMIT_JEDNEJ_PACZKI:
        ilosc_wyslanych_paczek += 1
        laczna_liczba_kilogramow += produkt
        paczka = 0
        print('Paczka jest pełna, pobierz nową paczkę')
    elif paczka > LIMIT_JEDNEJ_PACZKI:
        paczka -= produkt
        print(paczka)
        print(produkt)
        suma_pustych_kilogramow += LIMIT_JEDNEJ_PACZKI - paczka
        print(suma_pustych_kilogramow)
        laczna_liczba_kilogramow += paczka
        paczka = 0
        ilosc_wyslanych_paczek += 1
        print('Dodano produkt do paczki')
        print('Paczka jest pełna, pobierz nową paczkę')

if ilosc_wyslanych_paczek <= 1 :
    suma_pustych_kilogramow += LIMIT_JEDNEJ_PACZKI - paczka
    ilosc_wyslanych_paczek = 1
elif laczna_liczba_kilogramow == 20:
    ilosc_wyslanych_paczek = 1
else:
    laczna_liczba_kilogramow += paczka
    suma_pustych_kilogramow += LIMIT_JEDNEJ_PACZKI -paczka

# wyswietlenie wynikow

if ilosc_wyslanych_paczek == 1:
    print(f'Wysłano : {ilosc_wyslanych_paczek} paczkę')
elif ilosc_wyslanych_paczek > 1 or ilosc_wyslanych_paczek < 4 :
    print(f'Wysłano : {ilosc_wyslanych_paczek} paczki')
else:
    print(print(f'Wysłano : {ilosc_wyslanych_paczek} paczek'))
print(f'Wysłano : {laczna_liczba_kilogramow} kg')
print(f'Suma pustych kilogramów : {suma_pustych_kilogramow}')






