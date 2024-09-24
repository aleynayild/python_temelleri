#1 - Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz
# sayi= float(input('sayi: '))
# result= sayi>0 and sayi <100
#print(f'sayi 0-100 arasında mı: {result}')


#2 - girilen bir sayının pozitif mi negatif mi olduğunu kontrol ediniz
sayi = int(input('sayi:'))
result = (sayi > 0) and (sayi % 2 == 0)
print(f'sayının durumu: {result}')

#3- girilen 3 sayıyı büyüklük olarak karşılaştırınız
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

result = (a > b) and (a > c)
print(f'a en büyük sayıdır : {result}')

result = (b > a) and (b > c)
print(f' b en buyuk sayidir: { result}')
