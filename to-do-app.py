"""
I coded this program for my internship.
"""


#kullanıcıdan girdi almak ve ona menü sunman için fonksiyon.
#girdiği değeri kontrol ediyoruz.
def	girdi_al():
	"""Kullanıcıdan girdi almak için kullanılır."""
	print(
	"""
1- Görevleri Listele
2- Yeni Görev Ekle
3- Görev Düzenle
4- Görev Sil
5- Çıkış
	""")
	try:
		islem = int(input("Lütfen yapılacak işlemi seçiniz: "))
		if (islem >= 1 and islem <= 5):
			return (islem)
		else:
			raise ValueError

	except ValueError:
		print("Böyle bir seçenek yok.")

#bu fonksiyon dosyanın verisini getirmek için yazıldı.
#amaç veri getirmek olduğu için kip read.
def	veriyi_getir():
	try:
		with open("gorevler.txt", mode='r', encoding='utf-8') as file:
			sonuc = file.readlines()
		return (sonuc)
	except:
		return (list())

#gorevleri listeliyor.
#enumerate ile sayı veriyor.
def	gorevleri_listele(gorevler):
	"""Varsa görevleri ekranda listeler."""
	if (len(gorevler) == 0):
		print("Görev yok.")
		return 
	for i,j in enumerate(gorevler, start=1):
		print(str(i) + '- ' + j, end='')

# boş görev değilse dosyaya append ile ekliyorum. dosya yoksa diye + var.
def	yeni_gorev_ekle():
	"""Yeni görevi dosyaya yazar."""
	try:
		gorev = input("Yeni görevi giriniz: ")
		if (not len(gorev)):
			raise ValueError
		with open("gorevler.txt", mode='a+', encoding='utf-8') as file:
			file.write(gorev + '\n')
	except:
		print("Görev eklenemedi.")
	else:
		print("Görev eklendi.")

# görevleri listeye alıp listeden kaldırmak kolay oluyor.
# görev numarası ve diğer şeyler için try, except.
def	gorev_kaldir():
	"""Görevi siler."""
	try:
		gorev_numarasi = int(input("Silinecek görevin numarasını giriniz: "))
		if (gorev_numarasi <= 0):
			raise IndexError
		with open('gorevler.txt', mode='r+', encoding='utf-8') as file:
			gorevler = file.readlines()
			gorevler.pop(gorev_numarasi - 1)
			file.seek(0)
			file.truncate()
			file.writelines(gorevler)
	except ValueError:
		print("Silinecek görevin numarası sayı olmalıdır!")
	except IndexError:
		print("Girilen görev mevcut değil!")
	except:
		print("Görev silinemedi!")
	else:
		print("Görev silindi!")

#güncellemek için listeye alıp elemanı değiştirmek kolay geliyor.
#farklı bir yolu var mı emin olamadım.
def	gorev_guncelle():
	"""Seçilen görevi günceller."""
	try:
		gorev_numarasi = int(input("Güncellenecek görevin numarasını giriniz: "))
		if (gorev_numarasi <= 0):
			raise IndexError
		with open('gorevler.txt', mode='r+', encoding='utf-8') as file:
			gorevler = file.readlines()
			if (len(gorevler) < gorev_numarasi):
				raise IndexError
			gorevler[gorev_numarasi - 1] = input("Yeni görevi giriniz: ") + '\n'
			if (len(gorevler[gorev_numarasi - 1]) == 1):
				raise IndexError
			file.seek(0)
			file.truncate()
			file.writelines(gorevler)
	except ValueError:
		print("Güncellenecek görevin numarası sayı olmalıdır!")
	except IndexError:
		print("Girilen görev mevcut değil veya boş görev girdiniz!")
	except:
		print("Görev Güncellenemedi!")
	else:
		print("Görev Güncellendi!")

# çıktı ve girdi için ana görünüm burada oluşuyor.
def	ana():
	"""Program çalışmaya buradan başlar."""
	print("*** Görev Yönetim Uygulamasına Hoş Geldiniz ***")

	while True:
		gorevler = veriyi_getir()
		girdi = girdi_al()
		print("\n*****")
		if (girdi == 1):
			gorevleri_listele(gorevler)
		elif (girdi == 2):
			yeni_gorev_ekle()
		elif (girdi == 3):
			gorevleri_listele(gorevler)
			gorev_guncelle()
		elif (girdi == 4):
			gorevleri_listele(gorevler)
			gorev_kaldir()
		elif (girdi == 5):
			break
		print("*****")
	print("Programı kullandığınız için teşekkür ederiz.")

# şık durduğu için ekledim.
if __name__ == '__main__':
	ana()
