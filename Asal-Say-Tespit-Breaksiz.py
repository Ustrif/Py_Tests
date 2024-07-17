# 100 milyon ile 1 arasındaki asal sayıların tespiti için kullanılabilir.

while True:
    n = int(input("1 ile hangi sayının arasındaki asal sayıları bulmak istersiniz?: "))
    if n > 100000001:
        print("Geçersiz değer. Daha küçük sayı giriniz.")
    else:
        break

durum = 0
dene = 2
a = 0

for i in range(2,n+1):
    while i != dene:
        if i % dene == 0:
            durum = 1
        dene += 1

    dene = 2

    if durum == 0:
        print(f"{i}, ", end='')
        a += 1

    durum = 0

    if a % 25 == 0:
        print(end="\n")

print("sayıları asaldır.")
