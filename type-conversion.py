# x= input('1 sayi: ')
# y= input('2.sayi: ')

# toplam= int(x)+int(y)

# print(toplam)
x = 5             #int
y = 2.5           #float
name = 'cinar'    #string
isOnline = True   #bool

# print(type(x))
# print(type(y))
# print(type(name))
# print(type(isOnline))

# #type conversion
# #int to float

# x= float(x)
# print(x)
# print(type(x))

#örnek 1 soru 
"""
Daire alani :pi*r^2
Daire cevresi :2*pi*r
*yarıçapı verilen bir dairenin alanı ve çevresini hesaplayınız
r= 3.14

"""
pi = 3.14

yariCap =float(input ("yarı çap: "))
alan = pi * (yariCap ** 2)
cevre = 2* pi * yariCap

print("alan:",alan)
print("çevre:",cevre)