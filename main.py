#nadanie zmiennych
LIMIT_JEDNEJ_PACZKI = 20
ilosc_wyslanych_paczek = 0
laczna_liczba_kilogramow = 0
suma_pustych_kilogramow = 0
paczka = 0
najwiecej_pustych_kilogramow = 0
paczka_najwiecej_pustych_kilogramow = 0
nadmiar = 0

# wlasciwa czesc programu
liczba_produktow = int(input('Ile produktów chcesz wysłać?: '))
for _ in range(liczba_produktow):
    produkt = 0
    produkt = int(input('Paczka: Jestem wytrzymała, pakuj na maksa\nPodaj wagę produktu: '))
    paczka += produkt
    if produkt < 1 or produkt > 10:
        print('Produkt o nieodpowiedniej wadze!')
        break
    elif paczka < LIMIT_JEDNEJ_PACZKI:
        laczna_liczba_kilogramow += produkt
        continue
    elif paczka >= LIMIT_JEDNEJ_PACZKI:
        if paczka == LIMIT_JEDNEJ_PACZKI:
            laczna_liczba_kilogramow += produkt
            ilosc_wyslanych_paczek += 1
            paczka = 0
        if paczka > LIMIT_JEDNEJ_PACZKI:
            paczka -= produkt
            nadmiar = LIMIT_JEDNEJ_PACZKI - paczka
            suma_pustych_kilogramow += LIMIT_JEDNEJ_PACZKI - paczka
            laczna_liczba_kilogramow += produkt
            ilosc_wyslanych_paczek += 1
            paczka = produkt
            if nadmiar > najwiecej_pustych_kilogramow:
                najwiecej_pustych_kilogramow = nadmiar
                paczka_najwiecej_pustych_kilogramow = ilosc_wyslanych_paczek
                nadmiar = 0

if laczna_liczba_kilogramow <= 20 :
        suma_pustych_kilogramow += LIMIT_JEDNEJ_PACZKI - paczka
        ilosc_wyslanych_paczek =  1
        paczka_najwiecej_pustych_kilogramow = 1
if laczna_liczba_kilogramow % 20  == 0 :
        suma_pustych_kilogramow = 0
if laczna_liczba_kilogramow > 20 and  laczna_liczba_kilogramow % 20  != 0 :
        suma_pustych_kilogramow += LIMIT_JEDNEJ_PACZKI - paczka
        ilosc_wyslanych_paczek += 1

nadmiar = LIMIT_JEDNEJ_PACZKI - paczka
if nadmiar > najwiecej_pustych_kilogramow:
    paczka_najwiecej_pustych_kilogramow = ilosc_wyslanych_paczek

# wyswietlenie wynikow
print(f'Wysłano paczek : {ilosc_wyslanych_paczek} ')
print(f'Wysłano : {laczna_liczba_kilogramow} kg')
print(f'Suma pustych kilogramów : {suma_pustych_kilogramow}')
if suma_pustych_kilogramow != 0:
    print(f'Najwięcej pustych kilogramów ma paczka nr {paczka_najwiecej_pustych_kilogramow}[{nadmiar}kg]')
else:
    print('Wszystkie paczki zapakowane pod korek!')






