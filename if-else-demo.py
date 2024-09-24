#1- kullanıcıdan isim,yas ve egitim bilgilerini isteyip ehliyet alabilmee
#duurmunu kontrol ediniz.ehilyet alma kosulunu eb az 18 ve eğitim durumu 
# lise ya da üniveriste olmalıdır.

# isim = input ('isminiz: ')
# yas = int(input('yasiniz: '))
# egitim = input('egitim: ')
# if (yas>=18) and (egitim=='lise' or egitim=='üniversite') :
#  print('ehliyet alabilirsiniz.')
# else:
# print('ehliyet alamazsiniz.')

#2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan
#ortalamaya göre not aralığına karşılık gelen not bilgisini
#yazdırınız.

# yazili1 = float(input('1. yazılı notu: '))
# yazili2 = int(input('2. yazılı notu: '))
# sozlu = int(input('Sözlü notu: '))
# ortalama = float((yazili1 + yazili2 + sozlu) / 3)

# if (ortalama>=0) and (ortalama<25):
#   print(f'ortalamanız: {ortalama} notunuz: 0 ')
# elif (ortalama >= 25 )and (ortalama<45) :
#   print(f'ortalamanız: {ortalama} notunuz: 1 ')
# elif (ortalama >= 45 )and (ortalama<55) :
#   print(f'ortalamanız: {ortalama} notunuz: 2 ')
# elif (ortalama >= 55 )and (ortalama<70) :
#   print(f'ortalamanız: {ortalama} notunuz: 3 ')
# elif (ortalama >= 70 )and (ortalama<85) :
#   print(f'ortalamanız: {ortalama} notunuz: 4 ')
# elif (ortalama >= 85 )and (ortalama<100) :
#   print(f'ortalamanız: {ortalama} notunuz: 5 ')
# else:
#   print('yanlis bilgi girdiniz.')

#3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız
# 1.Bakım => 1.yıl
# 2.Bakım => 2.yıl
# 3.Bakım => 3.yıl
# *date time modulunu kullan

# days = int(input('Aracınız kaç gündür trafikte:'))  # input'u integer'a dönüştürüyoruz
# if days <= 365:
#     print('1. servis bakımı')
# elif 365 < days <= 365 * 2:  # aralıkları daha net göstermek için küçük bir düzenleme
#     print('2. servis bakımı')
# elif 365 * 2 < days <= 365 * 3:
#     print('3. servis bakımı')
# else:
#     print('Hatalı süre')




























