while True:
    sayi = int(input("Bir sayı girin: "))

    if sayi > 10:
        sonuc=sayi**2

    elif sayi<10 and sayi!=0:
        sonuc=sayi**3

    elif sayi==0:
        quit()

    print("Sonuç:", sonuc)

