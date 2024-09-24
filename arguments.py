# def changeName(n):
#     n = 'ada'

# name = 'yigit'

# changeName(name)
# print(name)

# def change(n):
#     n[0]='istanbul'
#     sehirler = ['ankara','izmir']
#     change(sehirler)
#     print(sehirler)

def add(*params):  # Burada *params sayesinde birden fazla argüman alınabilir
    sum = 0  # Toplamı tutmak için bir değişken oluşturuyoruz
    for n in params:  # params bir tuple ve her bir öğeyi n olarak alıyoruz
        sum = sum + n  # Her bir argümanı toplam değişkenine ekliyoruz
    return sum  # Sonuç olarak toplamı geri döndürüyoruz

print(add(10, 20, 30))  # 10 + 20 + 30 = 60 çıktısını verir


# #*params ve **params Arasındaki Fark:
# *params: İstediğin kadar pozisyonel argüman alır ve bunları bir tuple olarak işler.

# Örnek:


# def func(*params):
#     print(params)

# func(1, 2, 3)
# Çıktı: (1, 2, 3) → Pozisyonel argümanlar tuple içinde toplanır.

# **params: İstediğin kadar anahtar-değer (keyword) argümanı alır ve bunları bir sözlük olarak işler.

# Örnek:


# def func(**params):
#     print(params)

# func(a=1, b=2, c=3)
# Çıktı: {'a': 1, 'b': 2, 'c': 3} → Anahtar-değer argümanlar sözlük içinde toplanır.

# Özet:
# *params: Pozisyonel argümanlar alır (tuple içinde).
# **params: Anahtar-değer çiftleri alır (sözlük içinde).












