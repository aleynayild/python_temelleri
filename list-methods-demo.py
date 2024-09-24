names= ['Ali','Yağmur','Hakan','Deniz']
years =[1998,2000,1998,1987]
#1-Cenk ismini listenin sonuna ekleyeniz.
names.append('cenk')
print(names)
#2-Sena değerini listenin başına ekleyiniz
names.insert(0,'sena')
print(names)
#3-Deniz ismini listeden siliniz.
names.pop(4)
print(names)
#4-Ali listenin bir elemaanı var mıdır?
index= names.index('Ali')
print(index)
#5-liste elemanlarını tersine çevirin
names.reverse()
#6-liste elemanlarını alfabetik olarak sıralayınız.
names.sort()
#7-years listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()
#8-str ="chevrolet,dacia karakter dizisini listeye çeviriniz."



#9-years dizisinin en büyük ve en küçük elemanı nedir?
min =min(years)
max=max(years)
print(min,max)
#10-years dizisinde kaç tane 1998 değeri vardır?
result =years.count(1998)
#11-Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız 
markalar =[]
marka= input("marka: ")
markalar.append(marka)
print(markalar)