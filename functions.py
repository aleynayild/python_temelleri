def sayHello(name): #sayHello burada fonksiyon adıdır.
                    #" : " koymamızın sebebi yazdığımız şeylerin
                    #sayHello'ya ait olmasından dolayıdır.
                    #name isimli bir parametre alır ve tür aynı olmalıdır.
 print('Hello '+ name)
sayHello('Aleyna')
sayHello('Gökdeniz')
#sayHello() parametre belirtmezsek hata verir ve 3.sayHello() çalışmaz

#veya
def total(num1, num2):
  return num1+ num2 #print ile yazdırmadan değer döndürürüz.
result = total(10,20)
result = total(15,20)
print(result)

def yasHesapla(dogumYili):
  return 2024 - dogumYili
ageAleyna= yasHesapla(2004)

ageGokdeniz = yasHesapla(2004)

print(ageAleyna, ageGokdeniz)

def EmekliligeKacYilKaldi(dogumYili , isim):
      yas = yasHesapla(dogumYili)
      emeklilik = 65 - yas
      if emeklilik > 0:
         print(f'emekliliginize {emeklilik}yıl kaldı.')
      else:
         print('zaten emekli oldunuz')

EmekliligeKacYilKaldi(1980, 'Ali')






