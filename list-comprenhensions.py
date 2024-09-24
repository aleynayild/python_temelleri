# List Comprehensions (Liste Kapsamları), Python'da bir listeyi kısa ve okunaklı bir şekilde oluşturmanın bir yoludur.
# Normalde bir döngü ile listeye eleman eklemek yerine, list comprehension kullanarak bunu tek satırda yapabiliriz.
# Bu yöntem, Python kodunu daha kısa ve anlaşılır hale getirir.


# [ifade for öğe in iterable if koşul]
# ifade: Listede yer alacak elemanın ne olacağını belirtir.

# for öğe in iterable: Hangi iterable (örneğin, liste) üzerinden geçileceğini belirtir.
# if koşul: (Opsiyonel) Bir filtreleme koşulu eklenebilir. Eğer koşul doğruysa eleman listeye eklenir.
# Örnekler
# 1. Basit Liste Oluşturma
# Bir döngü kullanmadan 1'den 10'a kadar olan sayıları bir listeye ekleyelim:


# sayilar = [x for x in range(1, 11)]
# print(sayilar)


# Bu örnekte, for döngüsü ile 1'den 10'a kadar olan sayılar list comprehension kullanılarak oluşturuldu.

# 2. İfadenin Modifikasyonu
# Her bir sayının karesini alan bir liste oluşturabiliriz:


# kareler = [x**2 for x in range(1, 11)]
# print(kareler)

# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Burada x**2 ifadesi kullanılarak her sayı karesi ile listelendi.

# 3. Koşullu Liste Kapsamı (Filtreleme)
# Sadece çift sayıları alalım:


# cift_sayilar = [x for x in range(1, 11) if x % 2 == 0]
# print(cift_sayilar)

# [2, 4, 6, 8, 10]
# Bu örnekte, if x % 2 == 0 koşulu eklenerek sadece çift sayılar listeye dahil edildi.

# 4. Bir Listeyi Diğerine Dönüştürme
# Mevcut bir listedeki kelimeleri küçük harfe çeviren bir list comprehension yazalım:

# isimler = ["Ahmet", "MEHMET", "Ayşe"]
# kucuk_harfli = [isim.lower() for isim in isimler]
# print(kucuk_harfli)

# 5. İç İçe Döngüler
# List comprehension içinde birden fazla döngü de kullanabiliriz. Örneğin, iki liste arasındaki çarpımları bulalım:


# carpimlar = [x * y for x in range(1, 4) for y in range(1, 4)]
# print(carpimlar)


# [1, 2, 3, 2, 4, 6, 3, 6, 9]
# Burada iki döngü birden kullanılarak her x ve y kombinasyonunun çarpımı alındı.

# 6. İf-Else ile List Comprehensions
# Bir koşulda farklı değerler ekleyebiliriz. Örneğin, çift sayılara "çift", tek sayılara "tek" yazalım:


# sonuclar = ["çift" if x % 2 == 0 else "tek" for x in range(1, 6)]
# print(sonuclar)
