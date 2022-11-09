#sayının icindeki rakamların küplerinin toplamı sayıya eşit mi diye kontrol eder
top = 0


try:
    sayi = int(input("bir sayi giriniz: "))
    uzunluk = len(str(sayi))
    print(uzunluk)
    
    veri = str(sayi)
    
    for i in veri:
        top += int(i)**uzunluk
    
    if (sayi == top):
        print("hedefe ulasildi")
    else:
        print("basarisiz!!!")
    
except ValueError:
    print("hatali giris")