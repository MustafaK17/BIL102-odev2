import random

while True:
    try:
        giris = input("Lütfen bir sayı giriniz:")
        sayi=int(giris)

        if  100 > sayi > 10:
            sonuc=sayi**2

        elif 1000 >= sayi >= 100:
            bolen=random.randint(1,10)
            sonuc=sayi/bolen
            print("Bölen:", bolen)

        elif sayi < 0:
            sayi=-sayi
            sonuc=sayi

        elif sayi > 1000:
            bolen=random.randint(50,250)
            sonuc=sayi/bolen
            print("Bölen:", bolen)

        elif sayi<10 and sayi!=0:
            sonuc=sayi**3

        elif sayi==0:
            print("Kapatılıyor...")
            quit()


        print("Sonuç:", sonuc)

    except ValueError:
        print("Hatalı giriş yaptınız, lütfen bir sayı giriniz!")
