liczba_produktow = int(input('Ile produktow chcesz wysłać?: '))
liczba_paczek = 1
liczba_kilogramow = 0
liczba_pustych_kilogramow = 0
waga_przedmiotu = 0
idx = 0
if liczba_produktow =
for idx in range(liczba_produktow):
    waga_przedmiotu += int(input('Podaj wagę przedmiotu: '))
    waga_przedmiotu += liczba_kilogramow
    waga_przedmiotu -= waga_przedmiotu
    idx += 1
    if waga_przedmiotu >= 20:
        liczba_kilogramow -= liczba_kilogramow
        liczba_paczek += 1


print(liczba_kilogramow)
print(liczba_paczek)





