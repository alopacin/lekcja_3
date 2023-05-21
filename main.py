liczba_produktow = int(input('Ile produktow chcesz wysłać?: '))
ilosc_wyslanych_paczek = 1
laczna_liczba_kilogramow = 0
suma_pustych_kilogramow = 0
waga_przedmiotu = 0
idx = 0
jedna_paczka = 0

for idx in range(liczba_produktow):
    waga_przedmiotu += int(input('Podaj wagę przedmiotu: '))
    jedna_paczka += waga_przedmiotu
    if waga_przedmiotu < 1 or waga_przedmiotu > 10:
        break
    elif jedna_paczka < 20:
        laczna_liczba_kilogramow += waga_przedmiotu
        waga_przedmiotu -= waga_przedmiotu
    elif jedna_paczka > 20:
        laczna_liczba_kilogramow += waga_przedmiotu
        ilosc_wyslanych_paczek += 1
        jedna_paczka -= jedna_paczka
        suma_pustych_kilogramow += waga_przedmiotu
    elif jedna_paczka == 20 :
        laczna_liczba_kilogramow += waga_przedmiotu
        ilosc_wyslanych_paczek += 1
        jedna_paczka -= jedna_paczka
        waga_przedmiotu -= waga_przedmiotu


print(f'Wysłano : {laczna_liczba_kilogramow} kg')
print(f'Wysłano : {ilosc_wyslanych_paczek} paczek')
print(f'Suma pustych kilogramów: {suma_pustych_kilogramow}')





