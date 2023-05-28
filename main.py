#nadanie zmiennych

LIMIT_JEDNEJ_PACZKI = 20
ilosc_wyslanych_paczek = 1
laczna_liczba_kilogramow = 0
suma_pustych_kilogramow = 0
paczka = 0
najwieksza_ilosc_kilogramow =

# wlasciwa czesc programu
liczba_produktow = int(input('Ile produktów chcesz wysłać?: '))
for _ in range(liczba_produktow):
        produkt = 0
        produkt = int(input('Podaj wagę produktu: '))
        paczka += produkt

        if produkt < 1 or produkt > 10:
            break
        elif paczka < LIMIT_JEDNEJ_PACZKI:
            laczna_liczba_kilogramow += produkt
            print(f'Dodano produkt o wadze {produkt} kg do paczki')
        elif paczka == LIMIT_JEDNEJ_PACZKI:
            laczna_liczba_kilogramow += produkt
            paczka = 0
            ilosc_wyslanych_paczek += 1
            print('Paczka jest pełna, pobierz nową paczkę')
        elif paczka > LIMIT_JEDNEJ_PACZKI:
            paczka -= produkt
            print(paczka)
            print(produkt)
            suma_pustych_kilogramow += LIMIT_JEDNEJ_PACZKI - paczka
            print(suma_pustych_kilogramow)
            laczna_liczba_kilogramow += produkt
            ilosc_wyslanych_paczek += 1
            paczka = produkt
            print(paczka)
            print(produkt)
            print(f'Dodano produkt o wadze {produkt} kg do paczki')
            print('Paczka jest pełna, pobierz nową paczkę')


if laczna_liczba_kilogramow == LIMIT_JEDNEJ_PACZKI:
    ilosc_wyslanych_paczek = 1
    suma_pustych_kilogramow = 0
else:
    suma_pustych_kilogramow += LIMIT_JEDNEJ_PACZKI - paczka

#elif produkt != 0:
    #suma_pustych_kilogramow += LIMIT_JEDNEJ_PACZKI -paczka
    #laczna_liczba_kilogramow += produkt

# wyswietlenie wynikow

if ilosc_wyslanych_paczek == 1:
    print(f'Wysłano : {ilosc_wyslanych_paczek} paczkę')
elif ilosc_wyslanych_paczek > 1 or ilosc_wyslanych_paczek < 4 :
    print(f'Wysłano : {ilosc_wyslanych_paczek} paczki')
else:
    print(print(f'Wysłano : {ilosc_wyslanych_paczek} paczek'))
print(f'Wysłano : {laczna_liczba_kilogramow} kg')
print(f'Suma pustych kilogramów : {suma_pustych_kilogramow}')






