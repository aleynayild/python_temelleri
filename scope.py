x = 'global x'

def function():
    #local scope
    x = 'local x'
    print(x)

function()
print(x)

############################################
#global
name = 'Çınar'

def changeName(new_name):
     #local
     name=new_name
     print(name)
changeName('Ada')
print(name)

############################################
name = 'global string'

def greeting():
     #name = 'Çınar'
     def hello():
          print('hello'+name)
     hello()
greeting()

############################################

x = 50

def test(x):
    print('x: ' + str(x))  # x'i str tipine dönüştürüyoruz
    x = 100
    print('changed x to ' + str(x))  # x'i str tipine dönüştürüyoruz

test(x)  # Fonksiyonu çağırırken x değişkenini argüman olarak gönderiyoruz






