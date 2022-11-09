# belli bir sayıda ve belli bir aralıkta sayılar oluşturup  büyükten küçüğe sıralar

import random

liste = []

i=0
while (i < 20):
    liste.append(random.randint(0, 100))
    i += 1

print(liste)

yedek = 0
i = 0
j = 0

while (i <= 18):
    j = i+1
    
    while (j <= 19):
        if(liste[i] < liste[j]):
            yedek = liste[i]
            liste[i] = liste[j]
            liste[j] = yedek
        j += 1
    i += 1

print(liste)