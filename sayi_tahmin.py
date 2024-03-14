import time
import random
print("""Sayı Tahmin Oyunu 
1 ile 100 arasında(1 ve 100 dahil) rastgele tahmin edin. """)
a = 25
b = random.randint(1,100)

while True:
    tahmin =  int(input("Tahmin:"))

    if (tahmin == b):
        print("Tahmin doğrulanıyor.")
        time.sleep(1)
        print("Tebrikler!")
        print("Sayı",b)
        break
    elif(tahmin < b):
        print("Tahmin doğrulanıyor.")
        time.sleep(1)
        a -= 1
        print("Daha yüksek bir sayı söyleyin.")
        print("Tahmin Hakkı:",a)
    else:
        print("Tahmin doğrulanıyor.")
        time.sleep(1)
        a -= 1
        print("Daha düşük bir sayı söyleyin.")
        print("Tahmin Hakkı:",a)
    if (a == 0 ):
        print("Tahmin Hakkı Bitti.")
        print("Sayı:",b)
        break
input("Tıkla ve kapat.")



