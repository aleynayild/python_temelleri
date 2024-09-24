# 1-Gçnderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.

# def yazdir(kelime, adet):
#     print(kelime* adet)
# yazdir('merhaba\n ',10)


# 2-Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyon

# def listeye_cevir(*params):
#     liste = []
#     for param in params:
#         liste.append(param)
#         return liste
    
# result = listeye_cevir(10,20,30,'merhaba')
# print(result)


# 3-Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.

# def asalsayilaribul(sayi1, sayi2):
#     for sayi in range(sayi1, sayi2 + 1):
#         if sayi > 1:  # 1 asal sayı değildir.
#             for i in range(2, sayi):
#                 if (sayi % i == 0):  # Eğer sayı i'ye tam bölünüyorsa asal değildir.
#                     break
#             else:  # Döngü hiç 'break' yapmadıysa sayı asaldır
#                 print(sayi)

# sayi1 = int(input('sayi 1: '))
# sayi2 = int(input('sayi 2: '))

# asalsayilaribul(sayi1, sayi2)


# 4-Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürün.


def tambolenleribul(sayi):
    tambolenler = []
    for i in range(2, sayi):
        if sayi % i == 0:
            tambolenler.append(i)
    return tambolenler  # return döngünün dışına alındı

print(tambolenleribul(20))





