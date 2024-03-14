import time
print("""
*******************
Merhabalar,
Bu program bir ürünün kısaca fişini oluşturmaya yarıyor.
Kolay gelsin.

1- Yeni Fiş

2- Fişi Görüntüle

3- Fişi Düzenle

4- Fişi Sil


*******************""")

while True:
    işlemsayısı = int(input("İşlemin sayısını giriniz? : "))
    if (işlemsayısı == 1):
        print("Bekleyin lütfen...")
        time.sleep(1)
        ad = input("Adınız?: ")
        ürün = int(input("Fiyatı ne kadar?: "))
        adet = int(input("Kaç tane?: "))
        toplam = adet*ürün
        print("Bekleyin lütfen...")
        time.sleep(1)
        print("Kaydedildi.")
        with open("ürünlervedetaylar1.txt","w",encoding= "utf-8") as file:
            file.write("Adı= {} : Ürün Fiyatı= {} : Bu kadar= {}: Toplam {}\n".format(ad,ürün,adet,toplam))
            print("Dosya yazıldı.")

    elif (işlemsayısı == 2):
        print("Bekleyin lütfen...")
        time.sleep(1)
        with open("ürünlervedetaylar1.txt", "r", encoding="utf-8") as file:
            print("Dosyada hazırlanıyor..\n")
            time.sleep(1)
            oku = file.read()
            print(oku)

    elif (işlemsayısı == 3):
        with open("ürünlervedetaylar1.txt","r+",encoding="utf-8") as file:
            print("Bekleyin lütfen...")
            time.sleep(1)
            soru = int(input("Hangi satırı değiştirmek istiyorsunuz ? (Satırlar 0, 1 diye ilerler.) : "))
            liste = file.readlines()
            if soru >= len(liste):
                print("O kadar veri yoktur.")
            elif soru <= len(liste):
                ad = input("Adınız?: ")
                ürün = int(input("Fiyatı ne kadar?: "))
                adet = int(input("Kaç tane?: "))
                toplam = adet * ürün
                liste[soru] = ("Adı= {} : Ürün Fiyatı= {} : Bu kadar= {}: Toplam {}\n".format(ad,ürün,adet,toplam))
                with open("ürünlervedetaylar1.txt", "w",encoding= "utf-8") as file:
                    file.write("".join(liste))

    elif işlemsayısı == 4:
        with open("ürünlervedetaylar1.txt", "r+", encoding="utf-8") as file:
            soru = int(input("Hangi satırı silmek istiyorsunuz?(Satılar 0,1 diye gider.)"))
            liste = file.readlines()
            if soru >= len(liste):
                print("O kadar veri yoktur.")
            elif soru <= len(liste):
                liste[soru] = ("")
                with open("ürünlervedetaylar1.txt", "w",encoding= "utf-8") as file:
                    file.write("".join(liste))

