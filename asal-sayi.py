#girilen bir sayinin asal sayı olup olmadığını bulun.

# Kullanıcıdan bir sayı al
sayi = int(input("Bir sayı girin: "))

# Sayının asal olup olmadığını kontrol et
asal = True

# 1 ve negatif sayılar asal değildir
if sayi <= 1:
    asal = False
# 2 ve 3 asal sayılardır
elif sayi <= 3:
    asal = True
# 2 ve 3 dışında çift sayılar ve 3'e bölünebilen sayılar asal değildir
elif sayi % 2 == 0 or sayi % 3 == 0:
    asal = False
else:
    # 5'ten başlayarak sayının köküne kadar kontrol et
    i = 5
    while i * i <= sayi:
        if sayi % i == 0 or sayi % (i + 2) == 0:
            asal = False
            break
        i += 6

# Sonucu yazdır
if asal:
    print(f"{sayi} asal bir sayıdır.")
else:
    print(f"{sayi} asal bir sayı değildir.")








