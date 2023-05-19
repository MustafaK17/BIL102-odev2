import random

while True:
    sayi = int(input("Bir sayı girin: "))

    if  100 > sayi > 10:
        sonuc=sayi**2

    elif sayi >= 100:
        bolen=random.randint(1,10)
        sonuc=sayi/bolen
        print("Bölen:", bolen)

    elif sayi < 0:
        sayi=-sayi
        sonuc=sayi

    elif sayi<10 and sayi!=0:
        sonuc=sayi**3

    elif sayi==0:
        quit()

    print("Sonuç:", sonuc)

