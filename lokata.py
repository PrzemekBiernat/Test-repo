# -*- coding: utf-8 -*-

tytul=(('*'*10+'Lokata'+'*'*10))
print(tytul)
print('Symulacja lokaty 2,5%')
kapital_poczatkowy=float(input('Ile pieniędzy chcesz wpłacić na lokatę?'))
czas_lata=int(input('Na ile lat chcesz otworzyć loatę?'))
zysk=float(kapital_poczatkowy*0.25*czas_lata)
kapital_koncowy=kapital_poczatkowy + zysk

print('Twoje środki w wysokości {}zł przez {} lat urosną do {}zł.' .format(kapital_poczatkowy, czas_lata, kapital_koncowy))
print(tytul)
