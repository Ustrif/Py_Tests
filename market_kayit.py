import time
print("""Market Programına Hoş Geldiniz!

1. Verileri Girmek

2. Verileri Okumak 

3. Verileri Değiştirmek

4. Verileri Silmek

Yapımcı: "P4RS
""")


while True:
    veri = input("Hangi işlemi seçiyorsunuz?: ")
    if veri == "1":
        isim = input("Adınız: ")
        adet = int(input("Kaç adet aldınız?: "))
        fiyat = int(input("Fiyatı ne kadar?: "))
        toplam = adet*fiyat
        with open("market.txt","a",encoding="utf-8") as dosya:
            dosya.write("Isim: {} , Adet:{} , Fiyat:{} , Toplam:{}\n".format(isim,adet,fiyat,toplam))
            print("Dosya yazdırılıyor...\n")
    elif veri == "2":
        with open("market.txt","r",encoding="utf-8") as dosya:
            print("Dosyada ki veriler hazırlanıyor...\n")
            time.sleep(1)
            okuma = dosya.read()
            print(okuma)
        
    elif veri == "3":
        with open("market.txt","r+",encoding="utf-8") as dosya:
            print("Dosyada ki veriler hazırlanıyor...\n")
            time.sleep(1)
            soru = int(input("(Satırları görmek için '2' seçeneğine tıklayarak görebilirsiniz.) Hangi satırı değiştirmek istiyorsunuz?(Satırlar 0'dan başlamaktadır.): "))
            liste = dosya.readlines()
            if soru >= len(liste):
                print("O kadar satır veri yoktur. Lütfen tekrar deneyiniz.")
            elif soru <= len(liste):
                isim = input("Adınız: ")
                adet = int(input("Kaç adet aldınız?: "))
                fiyat = int(input("Fiyatı ne kadar?: "))
                toplam = adet*fiyat
                liste[soru] = ("Isim: {} , Adet:{} , Fiyat:{} , Toplam:{}\n".format(isim,adet,fiyat,toplam))
                with open("market.txt", "w") as dosya:
                    dosya.write("".join(liste))

            
    elif veri == "4":
        with open("market.txt","r+",encoding="utf-8") as dosya:
            print("Dosyada ki veriler hazırlanıyor...\n")
            time.sleep(1)
            soru = int(input("(Satırları görmek için '2' seçeneğine tıklayarak görebilirsiniz.) Hangi satırı silmek istiyorsunuz?(Satırlar 0'dan başlamaktadır.): "))
            liste = dosya.readlines()
            if soru >= len(liste):
                print("O kadar satır veri yoktur. Lütfen tekrar deneyiniz.")
            elif soru <= len(liste):
                liste[soru] = ("")
                with open("market.txt", "w") as dosya:
                    dosya.write("".join(liste))
    
    elif veri == "q":
        print("Programdan çıkılıyor...")
        input()
        break
        
    else:
        print("Yanlış değeri girdiniz.")




