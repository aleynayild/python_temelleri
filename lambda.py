# Bir sayının karesini alan normal fonksiyon
def square(num):
    return num ** 2

# Karelerini almak istediğimiz sayıların listesi
numbers = [1, 3, 5, 9]

# map() fonksiyonu ile 'square' fonksiyonunu 'numbers' listesindeki her elemana uyguluyoruz
result = map(square, numbers)

# 'result' bir map objesi olarak döner ve aşağıdaki döngüyle elemanları yazdırırız
for item in result:
    print(item)


# Lambda ile karesini alan bir fonksiyon tanımladık
numbers = [1, 3, 5, 9]
result = map(lambda num: num ** 2, numbers)

for item in result:
    print(item)

'''
lambda burada aslında sadece def ile tanımlanmış square fonksiyonunun yerine, kısa ve tek seferlik kullanım için daha pratik bir alternatif sunuyor.

'''


#Bir kere kullanılacak fonksiyonlar: Bir fonksiyonu sadece bir yerde ve kısa süreliğine kullanacaksan lambda, pratik bir çözümdür.
#map() Fonksiyonunun Kullanım Alanları
#Bir dizideki her bir elemanı dönüştürmek istediğimizde: Örneğin, bir sayı listesinin karelerini almak veya bir kelime listesini büyük harfe çevirmek.
#Matematiksel işlemler, string manipülasyonları, veri türü dönüşümleri gibi işlemler için kullanışlıdır.