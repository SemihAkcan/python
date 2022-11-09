#sayının bölenleri toplamı sayıya eşit mi diye kontrol eder

top = 0
liste = []

sayi = int(input("bir sayi giriniz: "))
i=1
while i < sayi:
    if (sayi % i == 0):
        top += i
        liste.append(i)
    i+=1
print(liste)
if (top==sayi):
    print("mukemmel sayi")
else:
    print("mükemmel sayi değil")